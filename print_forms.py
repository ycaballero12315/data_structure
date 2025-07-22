def get_base():
    base = int(input('Enter the base size (odd number): '))
    while base%2==0:
        base = int(input('Error: must be an odd number. Enter the base size: '))
    return base

def build_pattern(lines):
    return '\n'.join(lines)
    
def generate_triangle(base):
    return [(" " * ((base -i)//2) + '*'*i) for i in range(1, base + 1, 2)]

def generate_rombus(base):
    upper = generate_triangle(base)
    lower = [(" " * ((base -i)//2) + '*'*i) for i in range(base - 2, 0, -2)]
    return upper + lower
    
def generate_scuare(base):
    return ['*' * base for _ in range(base)]

def main():
    shape = input("Enter the shape (Triangle, Rhombus, Square): ").strip().lower()
    base = get_base()
    
    if shape == "triangle":
        print(build_pattern(generate_triangle(base)))
    elif shape == "rhombus":
        print(build_pattern(generate_rombus(base)))
    elif shape == "square":
        print(build_pattern(generate_scuare(base)))
    else:
        print("Unknown shape.")
        
if __name__=="__main__":
    main()