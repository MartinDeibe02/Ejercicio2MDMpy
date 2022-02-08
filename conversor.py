def leer_entero(texto):
    try:
        return int(input(texto))
    except ValueError:
        return None


if __name__ == '__main__':
    while True:
        print("""
CONVERSOR DE MONEDAS 
1. Dólares 
2. Libras 
3. Yen
0. Salir""")

        opcion = leer_entero("Escoja una opcion: ")

        if opcion == 1:
            pass
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 0:
            exit(0)
        else:
            print("Opcion no valida")