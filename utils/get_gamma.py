from math import acos, degrees

def get_gamma(c: int, d: int) -> float:
    gamma = degrees(acos(c/d))
    return gamma


