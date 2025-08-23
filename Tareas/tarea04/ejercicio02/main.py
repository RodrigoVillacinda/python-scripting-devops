#!/usr/bin/env python3


def main():
    sum = 0
    numero = 0
    while(numero != -1):
        numero = int(input("Ingrese un numero: "))
        if numero == -1:
            break
        sum += numero
    print("La suma de los numeros ingresados es: " + str(sum))


if __name__ == "__main__":
    main()
