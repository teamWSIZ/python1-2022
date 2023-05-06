from dataclasses import dataclass


@dataclass
class Fraction:
    # ułamek = numer / denom
    numer: int
    denom: int

    def value(self):
        return self.numer / self.denom

    def getDenominator(self) -> int:
        return self.denom

    def getNumerator(self) -> int:
        return self.numer


if __name__ == '__main__':
    f = Fraction(1, 2)
    assert f.value() == 0.5
