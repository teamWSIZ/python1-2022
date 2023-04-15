# Zadanie  : mamy listę string-ów... np. s=['aa', 'a', 'c', 'bb']; proszę napisać funkcję która sprawdzi,
# czy elementy tej listy są unikalne
 # podobnie jak w (A) -- ale w przypadku istnienia duplikatów proszę wypisać stringi które się powtarzają

s=['aa', 'a','c', 'bb']

def czy_sa_unikalne(w):

    s = set(w)

    if len(w) == len(s):

        return  True
    else:

     return False

def czy_sie_powtarzają(w):
    wyn = set()
    for x in w:
        if w.count(x) > 1: wyn.add(x)
    if len(wyn) ==0:
        return False
    return True, wyn



print(czy_sa_unikalne(s))
print(czy_sie_powtarzają(s))