def fib_rec(arr, elem, left, fkm1, fk, n):
    if fk == 0 or (fk == 1 and arr[left] != elem):
        if fk == 1:
            print(arr[left], end=' ')
        return None
    if fk == 1 and arr[left] == elem:
        print(arr[left], end=' ')
        return
    fkm2 = fk - fkm1
    mid = min(left + fkm2 - 1, n - 1)
    print(arr[mid], end=" ")

    if arr[mid] == elem:
        return
    if arr[mid] > elem:
        fib_rec(arr, elem, left, fkm1 - fkm2, fkm2, n)
    else:
        fib_rec(arr, elem, left + fkm2, fkm2, fkm1, n)


def fib(elem, arr):
    """
    >>> fib("8", "3 4 7 10 13 16 18 19")
    7 13 10 10
    """
    elem = int(elem)
    arr = list(map(int, arr.split()))
    if len(arr) == 0:
        print(None)
        return
    if elem > arr[-1] or elem < arr[0]:
        print(None)
    else:
        f1 = 0
        f2 = 1
        while len(arr) > f2:
            f1, f2 = f2, f1 + f2
        fib_rec(arr, elem, 0, f1, f2, len(arr))


elem = input()
arr = input()
fib(elem, arr)

