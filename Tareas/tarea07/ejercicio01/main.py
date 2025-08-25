#!/usr/bin/env python3


def main():
    myList = []
    x = 0
    print("------Input:------")
    while x != -1:
        x = int(input("Ingrese un numero: "))
        if x == -1:
            break
        myList.append(int(x))

    i = 0
    sum = 0
    for i in myList:
        sum += i
        print(i)

    sum = sum/len(myList)
    sum = int(sum)
    myList.insert(0, sum)

    j = 0
    print("------Output:------")
    for j in myList:
        print(j)


if __name__ == "__main__":
    main()
