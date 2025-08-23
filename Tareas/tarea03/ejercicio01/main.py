#!/usr/bin/env python3


def main():
    numero = input("Ingrese un numero: ")
    numero = int(numero)

    if numero < 100:
        print("Small")
    elif numero > 200:
        print("Large")
    else:
        print("Medium")


if __name__ == "__main__":
    main()
