def burble_sort(arr):
    n = len(arr)
    new_list = []
    for i in range(n):
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]           
    for i in arr:
        new_list.append(i)
    return new_list


arr = [7, 5, 4, 3]


print(burble_sort(arr))
   