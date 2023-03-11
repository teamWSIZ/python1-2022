#napisać funkcje: add(a,b) oraz mul(a,b) pierwsza zwracająca a+b, druga a*b.

def add(a,b):
    return (a+b)

def mul(a,b):
    return (a*b)

print(add(1,3))
print(mul(2,3))

# napisać funkcję calculate(fn, a, b)
# do której będziemy podawali jako pierwszy argument add albo mul, oraz dwie liczby, i która zwróci fn(a,b)

def calculate(fn, a, b):
    return fn(a,b)

print(calculate(add,2,4))
print(calculate(mul,5,6))