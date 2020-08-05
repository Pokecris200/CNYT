#Programa numeros a azar
#Cristian Camilo Forero
#29/04/2020
import random
def main():
    nombrea = input('Diga el nombre del archivo: ')
    arch = open(nombrea, "w")
    cantidad = int(input("Cantidad de lineas?: "))
    for i in range(cantidad):
        numx1 = random.randint(20,10000)
        linea = ""
        for j in range(numx1):
            num = random.randint(-1000,1000)
            linea += str(num) + ','
        num = random.randint(-1000,1000)
        linea += str(num)
        arch.write(linea + '\n')
    arch.close()
main()
