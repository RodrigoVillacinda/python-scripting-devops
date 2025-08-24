#!/usr/bin/env python3


def main():
    numero = 0
    suma = 0
    while numero != -1:
        suma += numero
        numero = int(input("Ingrese un numero: "))
    print("La suma de su numero es: " + '{0:8.2f}'.format(suma))


if __name__ == "__main__":
    main()
