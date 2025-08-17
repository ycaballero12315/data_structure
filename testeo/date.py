from datetime import datetime


now = datetime.now()

print(now.day)
print(now.hour)
print(now.min)

print(now.timestamp())

def find_missing(input_list):

  sum_of_elements = sum(input_list)
 
  # There is exactly 1 number missing
  n = len(input_list) + 1
  actual_sum = (n * ( n + 1 ) ) / 2
 
  return int(actual_sum - sum_of_elements)
list_1 = [1,5,6,3,4]


print(find_missing(list_1))