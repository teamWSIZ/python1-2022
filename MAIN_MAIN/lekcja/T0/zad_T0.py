import dataclasses


class ulamek_1:
    licznik_1 = int
    mianownik_1 = int


class ulamek_2:
    licznik_2 = int
    mianownik_2 = int


def dodawanie_ulamkow(liczniki_1, mianowniki_1, liczniki_2, mianowniki_2):
    if mianowniki_1 == mianowniki_2:
        suma_licznika = liczniki_1 + liczniki_2
        print("suma tych ułamów wynosi:", suma_licznika, "/", mianowniki_1)
    else:
        iloraz_licznika_1 = liczniki_1 * mianowniki_2
        iloraz_mianownika_1 = mianowniki_1 * mianowniki_2
        iloraz_licznika_2 = liczniki_2 * mianowniki_1
        iloraz_mianownika_2 = mianowniki_2 * mianowniki_1

        suma_licznikow = iloraz_licznika_2 + iloraz_licznika_1
        print("suma tych ułamów wynosi:", suma_licznikow, "/", iloraz_mianownika_2)


licznik_1, mianownik_1 = input(int)("Wpisz pierszy ułamek do dodawania")
licznik_2, mianownik_2 = input("Wpisz drógi ułamek do dodawania")
print(dodawanie_ulamkow(licznik_1, mianownik_1, licznik_2, mianownik_2))
