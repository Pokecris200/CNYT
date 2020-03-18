from Libreria1 import *
from Particula import *
def hermitiana(a):
    if a == matrixAdj(a):
        return True
    else:
        return False
def valorEsperado(observable, estado):
    aux = Accion(observable,estado)
    ve = transito(aux,estado)
    return ve

def varianza(matriz, ket):
    ve = valorEsperado(matriz,ket)
    m,n = len(matriz),len(matriz[0])
    b = ID(m,n)
    d = multiEscalarMatrix(b,multiplicacion(ve,(-1,0)))
    delta = sumaMatrix(matriz,d)
    preva = multiMatrix(delta,delta)
    var = valorEsperado(preva, ket)
    return var
    
