def two_sum(nums, target):
    seen = {}  # valor → índice
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return None

nums = [2, 7, 11, 15]
target = 9      
print(two_sum(nums, target))  # Salida: [0, 1]  