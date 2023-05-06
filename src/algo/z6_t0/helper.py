from model import Fraction


def add(f1: Fraction, f2: Fraction) -> Fraction:
    if f1.denom == f2.denom:
        return Fraction(f1.numer + f2.numer, f1.denom)

    newDenominator = f1.denom * f2.denom
    newF1Numerator = f1.numer * f2.denom
    newF2Numerator = f2.numer * f1.denom

    return Fraction(newF1Numerator + newF2Numerator, newDenominator)
