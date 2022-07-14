import FuncionesCaculos as Fx
import os


print("Bienvenido a la calculadora")

muestraMenu = True

while (muestraMenu):

    ingreso = input("Ingrese la opción a calcular:\n"
                    "1. Suma\n "
                    "2. Resta \n "
                    "3. Mutiplicación \n "
                    "4. Dividir \n "
                    "5. Salir \n ")

    NumA = int(input("Ingrese el primer numero\n"))
    NumB = int(input("Ingrese el segundo numero\n"))


    if (ingreso == "1"):
        print(Fx.Sumar(NumA,NumB))
    elif (ingreso == "2"):
        print(Fx.Restar(NumA, NumB))
    elif (ingreso == "3"):
        print(Fx.Multiplicar(NumA, NumB))
    elif (ingreso == "4"):
        print(Fx.Dividir(NumA, NumB))
    elif (ingreso == "5"):
        muestraMenu = False
        print("Gracias por utilizar nuestro Sistema")
    else:
        print("Ingrese una opción válida")


