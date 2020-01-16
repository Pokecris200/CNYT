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

d =(-2,1)
v =(1,2)
jo = (1,-1)
k = Suma(d,v)
#prettyPrinting(k)
#prettyPrinting(Suma(k,v))
l = multiplicacion (d, v)
#prettyPrinting(l)
m = div (d, v)
j = conj(v)
r = modulo (jo)
prettyPrinting(j)
print (modulo (jo))

print(Fase (v))
