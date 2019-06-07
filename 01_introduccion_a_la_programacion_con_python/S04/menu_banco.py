def mostrar_menu(saldo = 0):
    print("¡Bienvenido al Banco Amigo!. Escoja una opción:")
    print("1. Consultar saldo")
    print("2. Hacer depósito")
    print("3. Realizar giro")
    print("4. Salir")

def depositar(saldo, cantidad):
    return saldo + cantidad

def girar(saldo, cantidad):
    if cantidad > saldo:
        return False

    return saldo - cantidad

saldo_actual = 0

mostrar_menu(saldo_actual)
opcion = int(input("\n"))

while opcion != 4:
    if opcion == 1:
        print("\nSu saldo es de {}\n".format(saldo_actual))
    elif opcion == 2:
        cantidad = int(input("\n"))
        saldo_actual = depositar(saldo_actual, cantidad)
        print("\nSu nuevo saldo es de {}\n".format(saldo_actual))
    elif opcion == 3:
        if saldo_actual > 0:
            cantidad = int(input("\n"))
            resultado = girar(saldo_actual, cantidad)
            while resultado is False:
                print("\nNo se puede girar esta cantidad. Su saldo es de {}\n".format(saldo_actual))
                cantidad = int(input("\n"))
                resultado = girar(saldo_actual, cantidad)
            
            if resultado is not False:
                saldo_actual = resultado
                print("\nSu nuevo saldo es de {}\n".format(saldo_actual))
        else:
            print("\nNo puede realizar giros. Su saldo es 0\n")
    else:
        print("Opción inválida. Por favor ingrese 1, 2, 3 ó 4.")
    
    mostrar_menu(saldo_actual)
    opcion = int(input("\n"))


