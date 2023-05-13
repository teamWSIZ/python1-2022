from model import Fraction


def add(f1: Fraction, f2: Fraction) -> Fraction:
    f1.number = f1.number*f2.denominator + f2.number*f1.denominator
    f1.denominator = f1.denominator*f2.denominator
    
    return f1  
