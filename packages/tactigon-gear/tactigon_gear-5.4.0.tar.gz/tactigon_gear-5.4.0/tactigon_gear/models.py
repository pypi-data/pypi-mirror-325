from enum import Enum
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List

def get_or_default(json: dict, name: str, default):
    try:
        return json[name]
    except:
        return default

@dataclass
class Gesture:
    gesture: str
    probability: float
    confidence: float
    displacement: float

    def toJSON(self) -> dict:
        return {
            "gesture": self.gesture,
            "probability": self.probability,
            "confidence": self.confidence,
            "displacement": self.displacement,
        }

@dataclass
class Acceleration:
    x: float
    y: float
    z: float

    def toJSON(self) -> dict:
        return {
            "x": self.x,
            "y": self.y,
            "z": self.z,
        }


@dataclass
class Angle:
    roll: float
    pitch: float
    yaw: float

    def toJSON(self) -> dict:
        return {
            "roll": self.roll,
            "pitch": self.pitch,
            "yaw": self.yaw,
        }

@dataclass
class Gyro:
    x: float
    y: float
    z: float

    def toJSON(self) -> dict:
        return {
            "x": self.x,
            "y": self.y,
            "z": self.z,
        }

class OneFingerGesture(Enum):
    NONE = 0x00
    SINGLE_TAP = 0x01
    TAP_AND_HOLD = 0x02
    SWIPE_X_NEG = 0x04
    SWIPE_X_POS = 0x08
    SWIPE_Y_NEG = 0x20
    SWIPE_Y_POS = 0x10

class TwoFingerGesture(Enum):
    NONE = 0x00
    TWO_FINGER_TAP = 0x01
    SCROLL = 0x02
    ZOOM = 0x04


@dataclass
class Touch:
    one_finger: OneFingerGesture
    two_finger: TwoFingerGesture
    x_pos: float
    y_pos: float

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Touch):
            return (
                self.one_finger == __value.one_finger 
                and self.two_finger == __value.two_finger
                and self.x_pos == __value.x_pos
                and self.y_pos == __value.y_pos
            )
        
        return False
    
    def toJSON(self) -> dict:
        return {
            "one_finger": self.one_finger.value,
            "two_finger": self.two_finger.value,
            "x_pos": self.x_pos,
            "y_pos": self.y_pos
        }

class Hand(Enum):
    RIGHT = "right"
    LEFT = "left"

class TBleConnectionStatus(Enum):
    NONE = 0
    CONNECTING = 1
    CONNECTED = 2
    DISCONNECTING = 3
    DISCONNECTED = 4

class TBleSelector(Enum):
    NONE = 0
    SENSORS = 1
    AUDIO = 2

class AppType(Enum):
    GUI = 1
    CLI = 2

@dataclass
class TSkinState:
    connected: bool
    battery: float
    selector: Optional[TBleSelector]
    touchpad: Optional[Touch]
    angle: Optional[Angle]
    gesture: Optional[Gesture]

    def toJSON(self) -> dict:
        return {
            "connected": self.connected,
            "battery": self.battery,
            "selector": self.selector.value if self.selector else None,
            "touch": self.touchpad.toJSON() if self.touchpad else None,
            "angle": self.angle.toJSON() if self.angle else None,
            "gesture": self.gesture.toJSON() if self.gesture else None,
        }

@dataclass
class GestureConfig:
    model_path: str
    encoder_path: str
    name: str
    created_at: datetime
    gestures: Optional[List[str]] = None
    num_sample: int = 10
    gesture_prob_th: float = 0.85
    confidence_th: float = 5

    @classmethod
    def FromJSON(cls, json: dict):
        return cls(
            json["model_path"],
            json["encoder_path"],
            json["name"],
            datetime.fromisoformat(json["created_at"]),
            json["gestures"] if "gestures" in json else None,
            get_or_default(json, "num_sample", cls.num_sample),
            get_or_default(json, "gesture_prob_th", cls.gesture_prob_th),
            get_or_default(json, "confidence_th", cls.confidence_th)
            )
    
    def toJSON(self) -> dict:
        return {
            "model_path": self.model_path,
            "encoder_path": self.encoder_path,
            "name": self.name,
            "created_at": self.created_at.isoformat(),
            "gestures": self.gestures
        }

@dataclass
class TSkinConfig:
    address: str
    hand: Hand
    name: str = "Tactigon"
    gesture_config: Optional[GestureConfig] = None

    @classmethod
    def FromJSON(cls, json: dict):
        try:
            gesture_config = GestureConfig.FromJSON(json["gesture_config"])
        except:
            gesture_config = None

        return cls(
            json["address"], 
            Hand(json["hand"]),
            get_or_default(json, "name", cls.name), 
            gesture_config
        )
    
    def toJSON(self) -> dict:
        return {
            "address": self.address,
            "hand": self.hand.value,
            "name": self.name,
            "gesture_config": self.gesture_config.toJSON() if self.gesture_config else None,
        }