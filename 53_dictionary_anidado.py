def metodo1(dict1, dict2):
    return dict1 | dict2

def metodo2(dict1, dict2):
    combine_dict = dict1.copy()
    combine_dict.update(dict2)
    return combine_dict

def metodo3(dict1, dict2):
    conbined_dict = {key: dict1.get(key, 0) + dict2.get(key, 0) 
                     for key in set(dict1) | set(dict2)}
    
    return conbined_dict

def main():
    
    child1 = {
        "name": "Emil",
        "year": 2004
    }

    child2 = {
        "name": "Tobias",
        "year": 2007
    }
    
    print(f"metodo 3: {metodo3(child1, child2)}")
    print(f"metodo 2: {metodo2(child1, child2)}")
    print(f"metodo 1: {metodo1(child1, child2)}")
    
    
if __name__ == "__main__":
    main()

 
