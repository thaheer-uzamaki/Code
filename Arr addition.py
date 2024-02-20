def arr_add(arr):
    total = 0
    maxs = max(arr)
    arr.remove(maxs)
    for i in range(len(arr)):
        total += arr[i]
    if total >= maxs:
        print('TRUE')
    else:
        print('FALSE')

inp = list(map(int, input().split()))
arr_add(inp)