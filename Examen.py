#------------------------------------
import sys
def encabezado():
    print("Programacion 315");
    print("Examen");


encabezado()



def opcionUno():
    resUno = int(input("Digite su ingreso"));
    if (resUno > 0 and resUno < 1001):
        print("Estrato 1" + " su subsidio es de: " + str((resUno * 0.09)) )
    elif (resUno > 1000 and resUno < 1601):
        print("Estrato 2" + " su subsidio es de: " + str((resUno * 0.09)))
    elif (resUno > 1600 and resUno < 1902):
        print("Estrato 3")
    elif (resUno > 1901):
        print("Estrato 4")
    else:
        print("Error - Digite un ingreso valido")

def opcionDos():

    ventas = float(input("Digite el valor de ventas"))

    if(ventas < 40.000):
        print("Comision del vendedor: " + str(ventas *0.10))
    elif(ventas < 100.000):
        print("Comision del vendedor: " + str(ventas *0.21))

    elif(ventas < 200.000):
        print("Comision del vendedor: " + str(ventas *0.30))

    elif(ventas > 200.000):
        print("Comision del vendedor: " + str(ventas *0.32))

def opcionTres():
    nota = float(input("Digite su nota"));

    recibo = input("Entrego recibo de habilitacion? - Si, si es afirmativo")
    pago = input("Esta pago en el sistema? Si, si es afirmativo")

    if(nota >= 3.5 and nota <= 5.0 and recibo == "si" and pago == "si"):
        print("Aprobo habilitacion")
    else:
        print("No aprobo habilitacion")



def opcionCuatro():
    edad = int(input("Digite su edad"))

    if (edad < 16):
        print("No puede ingresar")
    elif(edad <= 18):
        print("Puede ingresar a zona zanahoria")
    elif(edad > 18):
        print("Puede ingresar a zona fuerte")
    else:
        print("Error, ingrese una edad valida")

def opcionCinco():
    print("Hasta luego")
    sys.exit()

respuestaC = "si"
while (respuestaC == "si"):
    print("Opcinoes");
    print("1. Estrato de personas");
    print("2. Valor comision ventas")
    print("3. Aprobacion asignaturas")
    print("4. Bar DMW")
    print("5. Salir del programa")


    respuesta = int(input('Digite el numero de su opcion'))
    if (respuesta == 1):
        opcionUno()
    elif (respuesta == 2):
        opcionDos()
    elif (respuesta == 3):
        opcionTres()
    elif (respuesta == 4):
        opcionCuatro()
    elif (respuesta == 5):
        opcionCinco()
    else:
        print("Digite un numero de opcion valido")

    respuestaC = (input("Desea escoger otra opcion?"))