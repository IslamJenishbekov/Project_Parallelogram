from math import acos, degrees

def get_beta(b: int, d: int) -> float:
    beta = degrees(acos(b/d))
    return beta


