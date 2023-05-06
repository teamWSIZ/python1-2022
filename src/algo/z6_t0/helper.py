from model import Fraction


def add(f1: Fraction, f2: Fraction) -> Fraction:
    if f1.getDenominator() == f2.getDenominator():
        return Fraction(f1.getNumerator() + f2.getNumerator(), f1.getDenominator())

    newDenominator = f1.getDenominator() * f2.getDenominator()
    newF1Numerator = f1.getNumerator() * f2.getDenominator()
    newF2Numerator = f2.getNumerator() * f1.getDenominator()

    return Fraction(newF1Numerator + newF2Numerator, newDenominator)
