def arithgeo(arr):
    if is_arithmetic(arr):
        return "Arithmetic"
    elif is_geometric(arr):
        return "Geometric"
    else:
        return -1

def is_arithmetic(arr):
    first_diff = arr[1] - arr[0]
    for num in range(len(arr) - 1):
        if arr[num + 1] - arr[num] != first_diff:
            return False
    return True

def is_geometric(arr):
    first_mul = arr[1] // arr[0]
    for num in range(len(arr) - 1):
        if arr[num + 1] // arr[num] != first_mul:
            return False
    return True

arr = list(map(int, input().split(",")))
arithgeo(arr)