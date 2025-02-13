import logging
import struct
import math
import asyncio

from bleak import BleakClient
from threading import Thread, Event, Lock
from multiprocessing.connection import _ConnectionBase

from typing import Optional

from ..models import  TBleSelector, Hand, Angle, Acceleration, Touch, Gyro, OneFingerGesture, TwoFingerGesture
from ..middleware.Tactigon_Audio import ADPCMEngine

class Ble(Thread):
    TICK: float = 0.02
    _RECONNECT_TIMEOUT: float = 0.1
    SENSORS_UUID: str = "bea5760d-503d-4920-b000-101e7306b005"
    TOUCHPAD_UUID: str = "bea5760d-503d-4920-b000-101e7306b009"
    AUDIO_DATA_UUID: str = "08000000-0001-11e1-ac36-0002a5d5c51b"
    AUDIO_SYNC_UUID: str = "40000000-0001-11e1-ac36-0002a5d5c51b"

    address: str
    hand: Hand
    debug: bool

    _stop_event: Event
    client: Optional[BleakClient]
    selector: TBleSelector
    _sensor_tx: Optional[_ConnectionBase] = None
    _angle_tx: Optional[_ConnectionBase] = None
    _audio_tx: Optional[_ConnectionBase] = None
    _update: Lock
    _update_touch: Lock
    _update_selector: Lock

    _angle: Optional[Angle] = None
    _acceleration: Optional[Acceleration] = None
    _gyro: Optional[Gyro] = None
    _battery: float = 0
    _touch: Optional[Touch] = None

    adpcm_engine: ADPCMEngine

    def __init__(self, address: str, hand: Hand, debug: bool = False):
        Thread.__init__(self, daemon=True)
        self.address = address
        self.hand = hand
        self.debug = debug

        self._stop_event = Event()
        self._update = Lock()
        self._update_touch = Lock()
        self._update_selector = Lock()
        self.client = None
        self.selector = TBleSelector.SENSORS
        self.adpcm_engine = ADPCMEngine()

    @staticmethod
    def gravity_comp(hand: Hand, accX: float, accY: float, accZ: float, gyroX: float, gyroY: float, gyroZ: float, roll: float, pitch: float, yaw: float):
        """gravity compensation"""
        G_CONST = 9.81
        ANG_TO_RAD = math.pi / 180
        ACC_RATIO = 1000
        VEL_RATIO = 30

        if hand == Hand.LEFT:
            accX = -accX / ACC_RATIO
            accY = -accY / ACC_RATIO
            accZ = -accZ / ACC_RATIO

            gyroX = -gyroX / VEL_RATIO
            gyroY = -gyroY / VEL_RATIO
            gyroZ = -gyroZ / VEL_RATIO

            _pitch = roll * ANG_TO_RAD
            _roll = pitch * ANG_TO_RAD

        else:
            accX = accX / ACC_RATIO
            accY = accY / ACC_RATIO
            accZ = -accZ / ACC_RATIO

            gyroX = gyroX / VEL_RATIO
            gyroY = gyroY / VEL_RATIO
            gyroZ = -gyroZ / VEL_RATIO

            _pitch = -roll * ANG_TO_RAD
            _roll = -pitch * ANG_TO_RAD

        if accZ == 0:
            beta = math.pi / 2
        else:
            beta = math.atan(
                math.sqrt(math.pow(accX, 2) + math.pow(accY, 2)) / accZ
            )

        accX = accX - G_CONST * math.sin(_roll)
        accY = accY + G_CONST * math.sin(_pitch)
        accZ = accZ - G_CONST * math.cos(beta)

        return accX, accY, accZ, gyroX, gyroY, gyroZ, roll, pitch, yaw

    @property
    def connected(self) -> bool:
        return (True if self.client.is_connected else False) if self.client else False
    
    @property
    def angle(self) -> Optional[Angle]:
        self._update.acquire()
        angle = self._angle
        self._update.release()
        return angle
    
    @property
    def acceleration(self) -> Optional[Acceleration]:
        self._update.acquire()
        acc = self._acceleration
        self._update.release()
        return acc

    @property
    def gyro(self) -> Optional[Gyro]:
        self._update.acquire()
        gyro = self._gyro
        self._update.release()
        return gyro
    
    @property
    def touch(self) -> Optional[Touch]:
        self._update_touch.acquire()
        touch = self._touch
        self._touch = None
        self._update_touch.release()
        return touch
        
    @property
    def battery(self) -> float:
        return self._battery

    def handle_audio_sync(self, char, data: bytearray):
        pass

    def handle_audio(self, char, data: bytearray):
        if self._audio_tx:
            self._audio_tx.send_bytes(self.adpcm_engine.extract_data(data))

    def handle_sensors(self, char, data:bytearray):
        accX = float(struct.unpack("h", data[0:2])[0])
        accY = float(struct.unpack("h", data[2:4])[0])
        accZ = float(struct.unpack("h", data[4:6])[0])
        
        gyroX = float(struct.unpack("h", data[6:8])[0])
        gyroY = float(struct.unpack("h", data[8:10])[0])
        gyroZ = float(struct.unpack("h", data[10:12])[0])
        
        roll = float(struct.unpack("h", data[12:14])[0])
        pitch = float(struct.unpack("h", data[14:16])[0])
        yaw = float(struct.unpack("h", data[16:18])[0])

        battery = int(struct.unpack("h", data[18:20])[0])

        accX, accY, accZ, gyroX, gyroY, gyroZ, roll, pitch, yaw = self.gravity_comp(self.hand, accX, accY, accZ, gyroX, gyroY, gyroZ, roll, pitch, yaw)

        self._update.acquire()

        self._angle = Angle(roll, pitch, yaw)
        self._acceleration = Acceleration(accX, accY, accZ)
        self._gyro = Gyro(gyroX, gyroY, gyroZ)
        self._battery = battery/1000

        self._update.release()

        if self.debug:
            logging.debug("Angle: %f,%f,%f",roll, pitch, yaw)
            logging.debug("Acceleration: %f,%f,%f",accX, accY, accZ)
            logging.debug("Gyro: %f,%f,%f",gyroX, gyroY, gyroZ)
            logging.debug("Battery: %f", battery/1000)

        if self._sensor_tx:
            self._sensor_tx.send([accX, accY, accZ, gyroX, gyroY, gyroZ])

        if self._angle_tx:
            self._angle_tx.send([roll, pitch, yaw])

    def handle_touchpad(self, char, data: bytearray):
        self._update_touch.acquire()
        one_finger = OneFingerGesture(int.from_bytes(data[0:1], "big"))
        two_finger = TwoFingerGesture(int.from_bytes(data[1:2], "big"))
        if one_finger is not OneFingerGesture.NONE or two_finger is not TwoFingerGesture.NONE:
            self._touch = Touch(
                one_finger,
                two_finger,
                float(struct.unpack("h", data[2:4])[0]),
                float(struct.unpack("h", data[4:6])[0])
            )
        self._update_touch.release()

    def start(self):
        logging.debug("[BLE] BLE starting on address %s", self.address)
        Thread.start(self)

    def join(self, timeout: Optional[float] = None):
        logging.debug("[BLE] Stopping BLE on address %s", self.address)
        self._stop_event.set()
        Thread.join(self, timeout)

    def run(self):
        asyncio.run(self.task())

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *attr):
        self.join()

    async def task(self):
        running_selector: Optional[TBleSelector] = None
        while not self._stop_event.is_set():
            self.client = BleakClient(self.address)
            try:
                await self.client.connect()
                await self.client.start_notify(self.TOUCHPAD_UUID, self.handle_touchpad)
                running_selector = None
            except Exception as e:
                logging.error("[BLE] Cannot connect to %s. %s", self.address, e)
                self.client = None
                await asyncio.sleep(self._RECONNECT_TIMEOUT)
                continue

            while self.connected:
                if self._stop_event.is_set():
                    await self.client.disconnect()
                    self.client = None
                    break

                if running_selector != self.selector:
                    self._update_selector.acquire()
                    if running_selector == TBleSelector.SENSORS:
                        await self.client.stop_notify(self.SENSORS_UUID)
                        self._update.acquire()
                        self._angle = None
                        self._acceleration = None
                        self._gyro = None
                        self._update.release()
                        logging.debug("[BLE] Stopped notification on sensors (%s)", self.SENSORS_UUID)
                    elif running_selector == TBleSelector.AUDIO:
                        await self.client.stop_notify(self.AUDIO_DATA_UUID)
                        await self.client.stop_notify(self.AUDIO_SYNC_UUID)
                        logging.debug("[BLE] Stopped notification on AUDIO (%s %s)", self.AUDIO_SYNC_UUID, self.AUDIO_DATA_UUID)

                    running_selector = self.selector

                    if running_selector == TBleSelector.SENSORS:
                        await self.client.start_notify(self.SENSORS_UUID, self.handle_sensors)
                        logging.debug("[BLE] Started notification on sensors (%s)", self.SENSORS_UUID)
                    elif running_selector == TBleSelector.AUDIO:
                        await self.client.start_notify(self.AUDIO_SYNC_UUID, self.handle_audio_sync)
                        await self.client.start_notify(self.AUDIO_DATA_UUID, self.handle_audio)
                        logging.debug("[BLE] Started notification on AUDIO (%s %s)", self.AUDIO_SYNC_UUID, self.AUDIO_DATA_UUID)
                    self._update_selector.release()                         

                await asyncio.sleep(self._RECONNECT_TIMEOUT)

            await asyncio.sleep(self._RECONNECT_TIMEOUT)       

    def select_sensors(self):
        self._update_selector.acquire()
        self.selector = TBleSelector.SENSORS
        self._update_selector.release()

    def select_audio(self):
        self._update_selector.acquire()
        self.selector = TBleSelector.AUDIO
        self._update_selector.release()

    def connect(self):
        self.start()

    def disconnect(self):
        self.join()

    def terminate(self):
        self.join()