opcion = ""

contador_mediciones = 0

while opcion != "4":
    print("\nSistema de Monitoreo de Contenido Hídrico de AgroTech Coop")
    print("\nMenu Principal: ")
    print("1. Registrar medición de contenido hidrico del suelo")
    print("2. Evaluación del nivel de humedad del suelo")
    print("3. Total de mediciones registradas")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    #registrar medicion
    if opcion == "1":
        print("\nRegistro del contenido hídrico del suelo (%): ")
        lote = int(input("Ingrese el numero de lote: "))
        cultivo = input("Ingrese el tipo de cultivo: ")
        porcentaje = int(input("Ingrese el porcentaje de contenido hídrico del suelo (%): "))
        fecha = input("Ingrese fecha y hora: ")
        contador_mediciones += 1  

    #recomendaciones segun humedad
    elif opcion == "2":
        print("\nEvaluación del Nivel de Humedad del Suelo")
        humedad = input("Ingrese el porcentaje de contenido hídrico del suelo (%): ")

        if humedad.isdigit():
            humedad = int(humedad)
            print("Contenido hidrico registrado:", humedad, "%")
            if humedad < 12:
                print("Recomendación: Humedad baja. Activar sistema de riego.")
            elif humedad >= 12 and humedad <= 15:
                print("Recomendación: Humedad optima. No hay recomendaciones")
            else:
                print("Recomendación: Humedad alta. Verificar drenaje del suelo y reducir la frecuencia de riego")
        else:
            print("Ingrese un numero entero.")

    #cantidad de mediciones
    elif opcion == "3":
        print("\nTotal de mediciones registradas:", contador_mediciones)

    #salir
    elif opcion == "4":
        print("\nSalir")
    else:
        print("Opción invalida. Intente nuevamente.")

