from bisect import bisect_left

def bisect_search(arr, elm):
    i = bisect_left(arr,elm)
    if i<=len(arr) and arr[i] == elm:
        return i
    else:
        return -1
    
if __name__ == "__main__":
    arr = [6,7,8,9,34,56,78]
    elm = 56
    result = bisect_search(arr, elm)
    if result != -1:
        print(f"El elemenrto {elm} esta en {result}")
    else:
        print(f'El elemento {elm} no existe en el array!')