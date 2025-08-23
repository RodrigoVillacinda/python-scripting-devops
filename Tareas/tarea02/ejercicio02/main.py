#!/usr/bin/env python3


def main():
    numero = 0
    print("Ingrese un numero: ")
    numero = input("")
    numero = int(numero)
    numero = round((numero/3), 3)
    print("El resultado es: " + str(numero))


if __name__ == "__main__":
    main()
