import dataclasses


class ulamek_1:
    licznik_1 = int
    mianownik_1 = int


class ulamek_2:
    licznik_2 = int
    mianownik_2 = int


def dodawanie_ulamków(licznik_1, mianownik_1, licznik_2, mianownik_2):
    if mianownik_1 == mianownik_2:
        suma_licznika = licznik_1 + licznik_2
        print("suma tych ułamów wynosi:", suma_licznika, "/", mianownik_1)
    else:
        iloraz_licznika_1 = licznik_1 * mianownik_2
        iloraz_mianownika_1 = mianownik_1 * mianownik_2
        iloraz_licznika_2 = licznik_2 * mianownik_1
        iloraz_mianownika_2 = mianownik_2 * mianownik_1

        suma_licznikow = iloraz_licznika_2 + iloraz_licznika_1
        print("suma tych ułamów wynosi:", suma_licznikow, "/", iloraz_mianownika_2)


print(dodawanie_ulamków(1, 2, 2, 5))
