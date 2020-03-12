from Libreria1 import *
def proba(a, pos):
    num = modulo(a[pos])
    den = norma(a)
    por = num/den
    round(por,2)
    return por
def transito(a,b):
    r = ProductIntVec(b,a)
    return r

