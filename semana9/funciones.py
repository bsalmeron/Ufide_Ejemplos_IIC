def ejemplo1():
    puntosJuego = [12, 45, 23, 23, 8, 4]

    for x in range(6):
        print(puntosJuego[x])
        if (puntosJuego[x] == 23):
            print("El numero es 23")
        else:
            print("El numero no es 23")





def ejemplo2():
    salario ={}
    cantidad = int (input("Cuantos salarios va ingresar: "))
    for x in range(0,cantidad):
        valor = int(input("Ingrese el salario: "))
        salario[x]=valor

    print("Monstrando lista de salarios ingresados")

    for y in range (0,len(salario)):
        print(salario[y], end=" ")
