from model import Fraction


def add(f1: Fraction, f2: Fraction) -> Fraction:
    n1 = f1.numer
    d1 = f1.denom
    n2 = f2.numer
    d2 = f2.denom
    f1.numer = n1*d2 + n2*d1
    f1.denom = d1*d2


    return f1  # obviously false
