from typing import Set

def difference_symetric(first_set: Set[int], second_set: Set[int])-> Set[int]:

    return first_set.symmetric_difference(second_set)

def difference_symetric_2(first_set: Set[int], second_set: Set[int])-> Set[int]:

    return first_set^second_set

first_set = {4,5,6,7,8}

second_set = {4,10,20,70,8}

print(f"La diferencia simetrica entre los dos conjuntos es: {difference_symetric(first_set, second_set)}")
print(f"La diferencia simetrica entre los dos aplicando la ^ conjuntos es: {difference_symetric_2(first_set, second_set)}")
