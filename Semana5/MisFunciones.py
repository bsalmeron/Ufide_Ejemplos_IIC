def mostrarDiezElementos():
    for i in range(5,50,10):
        print(i)


def mostrarNElementos(limite):
    for i in range(limite):
        if (i == 5):
            print("Hola mundo")
        print(i)


def TablaMultiplicar(tabla):
    for num in range(1,10):
        print(tabla, "x", num, " = ", num*tabla)


def bucleAnidado():
    for i in range(1,13):
        for j in range(1,13):
            print(i, "x", j, " = ", i*j)


