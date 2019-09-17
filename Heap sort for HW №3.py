def arr_to_str(arr):
    return " ".join(list(map(str, arr)))


def left_son(p):
    return 2 * p + 1


def right_son(p):
    return 2 * p + 2


def sift_down(arr, id):
    left = left_son(id)
    right = right_son(id)
    new = 0
    if left > len(arr) - 1:
        # Бездетный
        return arr
    elif right > len(arr) - 1:
        # Нету правого сына
        if arr[id] > arr[left]:
            arr[id], arr[left] = arr[left], arr[id]
        return arr
    # Есть оба сына
    if arr[id] < arr[left] and arr[id] < arr[right]:
        return arr
    elif arr[id] > arr[left] and arr[id] > arr[right]:
        if arr[right] > arr[left]:
            arr[id], arr[left] = arr[left], arr[id]
            new = left
        else:
            arr[id], arr[right] = arr[right], arr[id]
            new = right
    elif arr[left] < arr[id]:
        arr[id], arr[left] = arr[left], arr[id]
        new = left
    else:
        arr[id], arr[right] = arr[right], arr[id]
        new = right

    return sift_down(arr, new)


input_arr = input()
input_arr = list(map(int, input_arr.split()))


def Heap_sort(arr):
    i = len(arr) - 1
    while i != -1:
        sift_down(arr, i)
        i -= 1
        print(arr_to_str(arr))

    print()
    border = len(arr) - 1
    while border != -1:
        arr[0], arr[border] = arr[border], arr[0]
        arr[:border] = sift_down(arr[:border], 0)
        border -= 1
        print(arr_to_str(arr))


Heap_sort(input_arr)
