from __future__ import annotations
from dataclasses import dataclass
import math
from .math2d import Vec2, clamp, angle_to_unit


@dataclass
class CarSpec:
    max_speed: float = 900.0
    accel: float = 1200.0
    brake: float = 2000.0
    turn_rate: float = 2.6
    rolling_drag: float = 0.8
    linear_drag: float = 40.0

@dataclass
class CarState:
    pos: Vec2
    heading: float
    vel: Vec2


class Car:
    def __init__(self, spec: CarSpec, state: CarState) -> None:
        self.spec = spec
        self.state = state

        self.throttle: float = 0.0
        self.brake: float = 0.0
        self.steer: float = 0.0

        self.length = 46
        self.width = 22

    def set_inputs(self, throttle: float, brake: float, steer: float) -> None:
        self.throttle = clamp(throttle, 0.0, 1.0)
        self.brake = clamp(brake, 0.0, 1.0)
        self.steer = clamp(steer, -1.0, 1.0)

    def update(self, dt: float) -> None:
        s = self.state
        v = s.vel
        speed = v.length()

        speed_factor = clamp(speed / 250.0, 0.0, 1.0)
        s.heading += self.steer * speed_factor * self.spec.turn_rate * dt

        forward = angle_to_unit(s.heading)
        a_throttle = forward * (self.throttle * self.spec.accel)
        a_brake = forward * (-self.brake * self.spec.brake)

        if speed > 1e-6:
            drag_dir = v.normalized() * -1.0
        else:
            drag_dir = Vec2(0.0, 0.0)

        a_drag = drag_dir * (self.spec.rolling_drag * speed + self.spec.linear_drag)
        
        ax = a_throttle.x + a_brake.x + a_drag.x
        ay = a_throttle.y + a_brake.y + a_drag.y
            
    def get_polygon(self) -> list[Vec2]:
        pass