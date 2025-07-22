import csv

try:
    with open('file/weather.csv', 'r') as cs:
        reader = csv.DictReader(cs)
        
        found = False
        city = input('What City it search in the csv. ').strip().lower()
        for row in reader:
            if row['City'].strip().lower() == city:
                print(f'City: {row['City']}, Develoment: {row['Desarrollo']}; with an Per Cápita in the City: {row['Per Capita']}')
                found = True
                break
            
        if not found:
            print('Not found elemnt City in csv...')
            
except FileNotFoundError:
    print('No such file or directory')