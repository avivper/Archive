def rechead(n):
    if n == 0:
        return
    else:
        rechead(n - 1)
    print(n)


def rectail(n):
    if n == 0:
        return
    else:
        print(n)
    rectail(n - 1)


if __name__ == '__main__':
    print("Tail Recursion:")
    rectail(10)
    print("\nHead Recursion:")
    rechead(10)
