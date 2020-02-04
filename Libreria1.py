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
    mod = round (mod, 2)
    return mod

def Polar (a):
    f = (a[0]**2) + (a[1]**2)
    rho = math.sqrt (f)
    d = a[1] / a[0]
    Theta = math.atan2 (d)
    Theta = round (Theta,2)
    rho = round (rho ,2)
    return (rho, Theta)

def Fase (a):
    c = Polar (a)
    c = round (c,2)
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

def inversaMatrix(a):
    n,m = len(a),len(a[0])
    i = 0
    j = 0
    c = [[0 for j in range (m) ]for i in range (n)]
    for i in range (n):
            for j in range (m):
                c[i][j] = multiplicacion (a[i][j], (-1,0))
    return c

def multiEscalarMatrix (a, b):
    n,m = len(a),len(a[0])
    i = 0
    j = 0
    c = [[0 for j in range (m) ]for i in range (n)]
    for i in range (n):
            for j in range (m):
                c[i][j] = multiplicacion (a[i][j], b)
    return c

def matrixTrans (a):
    n,m = len(a),len(a[0])
    i = 0
    j = 0
    c = [[0 for j in range (m) ]for i in range (n)]
    for i in range (n):
            for j in range (m):
                c[i][j] = a [j][i]
    return c

def matrixConj (a):
    n,m = len(a),len(a[0])
    i = 0
    j = 0
    c = [[0 for j in range (m) ]for i in range (n)]
    for i in range (n):
            for j in range (m):
                c[i][j] = conj (a[i][j])
    return c

def matrixAdj (a):
    c = matrixTrans (matrixConj (a))
    return c

def multiMatrix (a, b):
    n,m = len(a),len(a[0])
    N = len(b)
    Aux =[]
    acum = []
    c = [[0 for j in range (m) ]for i in range (n)]
    if m == N :
        for i in range (n):
            for j in range (m):
                p = multiplicacion (a[i][j], b[j])
                Aux = Aux +[p]
                print(Aux)
                for k in range (len (Aux)-1):
                    c[i][j]= Suma (Aux[k], Aux [k+1])
                    print (c)
    return c

def ProductInt (a, b):
    Mat1 = matrixAdj (a)
    
    return

def Accion (a, b):
    Vec = []
    Aux =[]
    n,m = len(a),len(a[0])
    B = len (b)
    if B == m:
         for i in range (n):
            for j in range (m):
                p = multiplicacion (a[i][j], b[j])
                Aux = Aux +[p]
            x = Suma (Aux[0], Aux[1])
            x
    return Vec

#prettyPrinting(multiplicacion ((6,1),(1,2)))
#prettyPrinting(multiplicacion ((5,2),(3,5)))
#prettyPrinting(Suma (multiplicacion ((6,1),(1,2)), multiplicacion ((5,2),(3,5))))
l = [(1,2),(3,5)]
mat1 = [[(7,3),(4,2)], [(6,1),(5,2)]]
'''w = [[(7,3),(4,2)], [(6,1),(5,2)]]
d =(3,4)
#print(sumaMatrix(w,mat1))
v =(-1,0)
print(matrixAdj(w))
#prettyPrinting(multiplicacion (d,v))
#prettyPrinting(multiplicacion (c,g))
#x = (0,-1)
#y = (1,0)
#prettyPrinting(Suma (multiplicacion (d,v),multiplicacion (c,g)))
#print(Fase (v))'''
print(multiMatrix(mat1, l))
