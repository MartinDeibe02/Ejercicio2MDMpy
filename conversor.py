from monedas import Dolar, Libra, Yen


def leer_entero(texto):
    try:
        return int(input(texto))
    except ValueError:
        return None


def texto_valor():
    print("Escriba la cantidad: ", end="")


def leer_valor():
    try:
        return float(input())
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
            texto_valor()
            leer_cantidad = leer_valor()

            if isinstance(leer_cantidad, float):
                moneda = Dolar(leer_cantidad)
                print(f'La cantidad en euros es {Dolar.cantidadEnEuros(moneda)}')
            else:
                print("Introduzca un numero valido")
                
        elif opcion == 2:

            texto_valor()
            leer_cantidad = leer_valor()

            if isinstance(leer_cantidad, float):
                moneda = Libra(leer_cantidad)
                print(f'La cantidad en euros es {Libra.cantidadEnEuros(moneda)}')
            else:
                print("Introduzca un numero valido")

        elif opcion == 3:

            texto_valor()
            leer_cantidad = leer_valor()

            if isinstance(leer_cantidad, float):
                moneda = Yen(leer_cantidad)
                print(f'La cantidad en euros es {Yen.cantidadEnEuros(moneda)}')
            else:
                print("Introduzca un numero valido")

        elif opcion == 0:
            exit(0)
        else:
            print("Opcion no valida")
