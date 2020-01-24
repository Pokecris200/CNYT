import math

def Suma (a, b):
    return (a[0]+b[0], a[1]+ b[1])
def prettyPrinting(a):
    if a[1]>=0 :
        print(a[0],"+",a[1],"i")
    else :
        print(a[0],a[1],"i")
def resta(a, b):
    return (a[0]-b[0], a[1]-b[1])
def multiplicacion (a, b):
    First = (a[0]*b[0])-(a[1]*b[1])
    Second = (a[0]*b[1])+(a[1]*b[0])
    return(First, Second)
def div (a,b):
    num1 = (a[0]*b[0])+(a[1]*b[1])
    den = (b[0]**2)+(b[1]**2)
    num2 =(b[0]*a[1])-(a[0]*b[1]) 
    return ((num1/den), (num2/den))
def conj (a):
    Conjugado = (a[1] * (-1))
    return (a[0], Conjugado)
def modulo (a):
    rad = (a[0]**2) + (a[1]**2)
    mod = math.sqrt (rad)
    return mod
def Polar (a):
    f = (a[0]**2) + (a[1]**2)
    rho = math.sqrt (f)
    d = a[1] / a[0]
    Theta = math.atan (d)
    return (rho, Theta)
def Fase (a):
    c = Polar (a)
    return c[1]
def sumaVect(a,b):
    matriz = []
    i = 0
    for i in range(len(a)):
        matriz = matriz + [Suma (a[i],b[i])]
    return matriz
def inversaVect(a):
    matriz = []
    i = 0
    s = (-1,0)
    for i in range(len(a)):
        matriz = matriz + [multiplicacion (a[i], s)]
    return matriz
def productoEscalarV(a, b):
    matriz = []
    i = 0
    for i in range(len(a)):
        matriz = matriz + [multiplicacion (a[i], b)]
    return matriz
def sumaMatrix (a, b):
    i = 0
    j = 0
    n,m = len(a),len(a[0])
    N,M = len(b),len(b[0])
    
    if n == N and m == M:
        c = [[0 for j in range (m) ]for i in range (n)]
        for i in range (n):
            for j in range (m):
                c[i][j] = Suma (a[i][j], b[i][j])
    return c

    


w = [(7,3),(4,2)]
l = [(1,2),(3,5)]

d =(3,4)
v =(-1,0)
print(productoEscalarV(w,v))
#prettyPrinting(multiplicacion (d,v))
c =(-1,0)
g = (-1,0)
#prettyPrinting(multiplicacion (c,g))
#x = (0,-1)
#y = (1,0)
#prettyPrinting(multiplicacion (x,y))
#prettyPrinting(Suma (multiplicacion (d,v),multiplicacion (c,g)))
print(Fase (v))
