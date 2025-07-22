feet_inches = input("Enter de feet and inches: ")

def destructurin_feet_inch(feet_inches):
    parts = feet_inches.split(' ')
    feet = float(parts[0])
    inch = float(parts[1])
    return feet, inch

def convert_meter(feet, inch):
    convert = feet * 0.348 + inch * 0.0254
    return convert

feet, inch = destructurin_feet_inch(feet_inches)

result = convert_meter(feet, inch)

if result< 1:
    print('Kid is too small!')
else:
    print('Kid can use the slide!')
    