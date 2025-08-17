import json as js
import csv
from openpyxl import Workbook
import xml.etree.ElementTree as TR
import re

with open('../file/prueba.txt', 'r+') as file_format:
    for f in file_format.readlines():
        print(f)

elem = {'name': "Yoeny", 
        'lastname': 'Caballero',
        'age': 41,
        'languaje': ["Python", "Kotlin", "Swift"]}

data = [
    {'name': 'Nikhil', 'branch': 'COE', 'year': 2, 'cgpa': 9.0},
    {'name': 'Sanchit', 'branch': 'COE', 'year': 2, 'cgpa': 9.1},
    {'name': 'Aditya', 'branch': 'IT', 'year': 2, 'cgpa': 9.3},
    {'name': 'Sagar', 'branch': 'SE', 'year': 1, 'cgpa': 9.5},
    {'name': 'Prateek', 'branch': 'MCE', 'year': 3, 'cgpa': 7.8},
    {'name': 'Sahil', 'branch': 'EP', 'year': 2, 'cgpa': 9.1}
]

with open('../file/test.json', 'w+') as file:
    js.dump(elem, file, indent = 4)
    file.seek(0)
    for i in file.readlines():
        print(i)

with open('../file/test.cvs', 'w+', newline='') as file_csv:
    fieldname = ['name', 'branch', 'year', 'cgpa']
    writer = csv.DictWriter(file_csv, fieldnames=fieldname)
    writer.writeheader()
    writer.writerows(data)
    file_csv.seek(0)
    for elem in file_csv.readlines():
        print(elem)

# writer and read excel
nuevo = Workbook()
hoja = nuevo.active
hoja.title = "Data"
hoja['A1'] = 'Nombre'
hoja['B1'] = 'Edad'
hoja.append(['Yoe', 41])
hoja.append(['Duni', 44])
nuevo.save('../file/test.xls')

# --- Reading an XML file ---
try:
    tree = TR.parse('example.xml')
    root = tree.getroot()

    print("Root tag:", root.tag)

    for child in root:
        print(f"  Child tag: {child.tag}, text: {child.text}, attributes: {child.attrib}")

except FileNotFoundError:
    print("example.xml not found. Creating a sample XML for demonstration.")
    # Create a sample XML if it doesn't exist
    root = TR.Element("data")
    record1 = TR.SubElement(root, "record", id="1")
    rid1 = TR.SubElement(record1, "rid")
    rid1.text = "1"
    name1 = TR.SubElement(record1, "name")
    name1.text = "Record 1"

    record2 = TR.SubElement(root, "record", id="2")
    rid2 = TR.SubElement(record2, "rid")
    rid2.text = "2"
    name2 = TR.SubElement(record2, "name")
    name2.text = "Record 2"

    tree = TR.ElementTree(root)
    tree.write('../file/example.xml', encoding='utf-8', xml_declaration=True)
    print("example.xml created. Please run the script again to read it.")
    exit()

# --- Modifying and writing an XML file ---
# Find a specific element and modify its text and add an attribute
for record in root.findall('record'):
    if record.get('id') == '1':
        name_element = record.find('name')
        if name_element is not None:
            name_element.text = "Updated Record 1 Name"
            name_element.set('status', 'modified')

# Add a new element
new_record = TR.SubElement(root, "record", id="3")
new_rid = TR.SubElement(new_record, "rid")
new_rid.text = "3"
new_name = TR.SubElement(new_record, "name")
new_name.text = "New Record 3"

# Write the modified tree to a new file
tree.write('../file/modified_example.xml', encoding='utf-8', xml_declaration=True)
print("\nModified XML written to modified_example.xml")
