def DNF(arr_size, arr):
    low = 0
    mid = 0
    high = arr_size - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr


def p(arr):
    for i in arr:
        print(i, end=" ")


arr = [0, 1, 1, 0, 0, 2, 0, 2, 1]
arr_size = len(arr)
DNF(arr_size, arr)
p(arr)
