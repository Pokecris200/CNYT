from Libreria1 import *
def proba(a, pos):
    num = modulo(a[pos])
    den = norma(a)
    por = (num**2)/(den**2)
    round(por,2)
    return por
def transito(a,b):
    r = ProductIntVec(b,a)
    return r

