from model import Fraction


def add(f1: Fraction, f2: Fraction) -> Fraction:
    a = f1.numer*f2.denom + f2.numer*f1.denom
    b = f1.denom*f2.denom
    res = Fraction(a, b)
    return res
