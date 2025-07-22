def count_character_upper(name):
    try:
        with open(f'blog_api/app/file/{name}', 'r') as f:
            txt = f.readlines()
            count = sum(1 for line in txt for chrt in line if chrt.isupper())
        return count
    except FileNotFoundError:
        return "File not Found"


print(count_character_upper('name.txt'))