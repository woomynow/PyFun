def bubble_sort(arr):
    for p in range(len(arr) - 1):
        for n in range(len(arr) - p - 1):
            if arr[n] > arr[n + 1]:
                swap(arr, n)
                
def swap(arr, n):
    tmp = arr[n + 1] 
    arr[n + 1] = arr[n]
    arr[n] = tmp

numbers = [7, 3, 5, 9, 1]

bubble_sort(numbers)
print(numbers)