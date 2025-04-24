from collections import defaultdict, Counter

def dict_create_with_list(list_num):
    dict_number = {}
    for i in list_num:
        if i in dict_number:
            dict_number[i] +=1
        else:
            dict_number[i] = 1

    return dict_number

#Metodo hace lo mismo
def dict_create_with_list_use_module(list_num):
    dict_number = defaultdict(int)
    for elem in list_num:
        dict_number[elem] +=1
    return dict_number

#Mas resumido, pero menos especifico
def dict_create_with_list_use_module_c(list_num):
    return dict(Counter(list_num))

def main():
    list_num = [3,4,5,6,6,6]
    dict_num = dict_create_with_list(list_num)

    for num, cant in dict_num.items():
        print(f"{num}: {cant}")
    
    print("\n")
    dict_num_defaultdict = dict_create_with_list_use_module(list_num)
    for num, cant in dict_num_defaultdict.items():
        print(f"{num}: {cant}")
    
    print("\n")
    dict_num_counter = dict_create_with_list_use_module_c(list_num)
    for num, cant in dict_num_counter.items():
        print(f"{num}: {cant}")

if __name__ == "__main__":
    main()