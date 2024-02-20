#bubble sort
def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
my_array=[9,7,10,5,3,8,12,1]
bubble_sort(my_array)
print(my_array)