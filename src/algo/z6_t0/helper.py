from model import Fraction


def add(f1: Fraction, f2: Fraction) -> Fraction:

    f1.numer = f1.numer*f2.denom + f2.numer*f1.denom
    f1.denom = f1.denom*f2.denom

    return f1
