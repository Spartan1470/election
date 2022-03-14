print("Conteo De Votos\n\n")
opcion = 0
opcion2 = 0

senado= 0
camara = 0
pacto = 0
centro = 0
derecha = 0

while(opcion != 4):
    print("\n1)Senado\n2)Camara\n3)Consulta\n4)salir\n5)Mostrar votos")
    opcion = int(input("Ingrese una opcion del menu: "))
    if opcion == 1:
        senado += 1 
    elif opcion == 2:
        camara += 1
    elif opcion == 3:
        print("\n  1)pacto\n  2)centro\n  3)derecha\n  4)salir\n")
        opcion2 = int(input("Ingrese una opcion: "))
        if opcion2 == 1:
            pacto += 1
        elif opcion2 == 2:
            centro += 1
        elif opcion2 == 3:
            derecha += 1
    elif opcion == 5:
        print(f'Senado: {senado}\nCamara: {camara}\nPacto: {pacto}\nCentro: {centro}\nDerecha: {derecha}')   


            




    