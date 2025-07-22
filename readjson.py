import json

try:
    with open('file/questions.json', 'r') as js:
        content = js.read()
except FileNotFoundError:
    print('Fichero no encontrado. ')

data = json.loads(content)

for question in data:
    print(question['question_text'])
    for index, alternative in enumerate(question['alternatives'], 1):
        print(f'{index} - {alternative}')
    user_choice = int(input('Enter your answer: '))
    if user_choice == 3:
        print(f"It is: {data[0]['alternatives'][user_choice-1]}")
    elif user_choice == 2:
        print(f"It is: {data[1]['alternatives'][user_choice-1]}")
    else:
        print('Not Found')