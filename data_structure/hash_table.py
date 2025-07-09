from collections import defaultdict


texto = 'hello yo soy el texto largo que tienen que picar por el espacio'

contexto = defaultdict(int)

for palabra in texto.split(" "):
    contexto[palabra] += 1