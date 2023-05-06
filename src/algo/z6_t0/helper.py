from model import Fraction

def add(f1: Fraction, f2: Fraction) -> Fraction:
    f11, f12 = (f1.numer, f1.denom)
    f21, f22 = (f2.numer, f2.denom)

    out = f11 + f21

    return Fraction(out, f12)

