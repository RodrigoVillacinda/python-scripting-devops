#!/usr/bin/env python3
from datetime import datetime
from datetime import timedelta

def main():
    x = int(input("Ingrese un numero: "))
    now = datetime.now() + timedelta(days=x) 
    print(now.strftime("%A, %B %d, %Y"))


if __name__ == "__main__":
    main()
