from __future__ import annotations
from dataclasses import dataclass
import math


@dataclass(frozen=True)
class Vec2:
    x: float
    y: float

    def __add__(self, other: "Vec2") -> "Vec2":
        return Vec2(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: "Vec2") -> "Vec2":
        return Vec2(self.x - other.x, self.y - other.y)
    
    def __mul__(self, k : float) -> "Vec2":
        return Vec2(k * self.x, k * self.y)
    
    def length(self):
        return math.hypot(self.x, self.y)
    
    def normalized(self):
        L = self.length()
        if L <= 1e-9:
            return Vec2(0.0, 0.0)
        return Vec2(self.x / L, self.y / L)
    

def clamp(x: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, x))


def angle_to_unit(theta: float) -> Vec2:
    return Vec2(math.cos(theta), math.sin(theta))