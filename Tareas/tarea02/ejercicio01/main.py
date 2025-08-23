#!/usr/bin/env python3
import math


def main():
    salario = 0
    print("Ingrese su salario: ")
    salario = input("")
    salario = int(salario)
    print("Su salario anual es de:   " + str(salario))
    salario = int(math.ceil(salario/12))
    print("Su salario mensual es de: " + str(salario))


if __name__ == "__main__":
    main()
