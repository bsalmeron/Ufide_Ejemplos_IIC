

def evaluacion_ingreso():
    opcion_menu=True
    while (opcion_menu):
        evaluacion_edad()
        # Menu
        opcion_menu= menu()
    #Sale del sistema
    despedida()


def evaluacion_edad():
    # Entradas de datos
    Edad = int(input("Ingrese la edad "))

    if (Edad >= 18):
        print("\n\n***********************")
        print("*Puede ingresar al bar *")
        print("***********************\n\n")
        ambiente_musical = input("Cual ritmo o area desa ingresar ")
        if (ambiente_musical == "Rock"):
            print("Ingresando al salón de rock ")
        elif (ambiente_musical == "Cumbia"):
            print("Ingresando al salón de cumbia")
        elif (ambiente_musical == "Mariachi"):
            print("Ingresando al salón de mariachi")
        elif (ambiente_musical == "house"):
            print("Ingresando al salón de house")
        elif (ambiente_musical == "Reggae"):
            print("Ingresando al salón de reggae")
        else:
            print("Lo siento no existe ese ritmo")
    else:
        print("Es menor de edad")


def menu():
    repsuesta_menu = int(input("\n\n¿Desea evaluar el ingreso de otra persona? SI= 1 / NO =0 ---> "))
    if (repsuesta_menu == 0):
        valor = False
    else:
        valor = True
    return valor

def despedida():
    print("Gracias por usar el sistema")