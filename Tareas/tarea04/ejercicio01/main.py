#!/usr/bin/env python3


def main():
    numero = input("Ingrese un numero: ")
    numero = int(numero)
    sum = 0
    numero = numero + 1
    for x in range(numero):
        sum += x
        x += 1
    print("La suma es: " + str(sum))


if __name__ == "__main__":
    main()
