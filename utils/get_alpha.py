from math import acos, degrees

def get_alpha(a: int, d: int) -> float:
    alpha = degrees(acos(a/d))
    return alpha


