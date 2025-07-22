def insert_sort_test(arr):
    n = len(arr)
    if n <= 1:
        return
    
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


arr = [6,4,2,8,9]

insert_sort_test(arr)

print(arr)
            