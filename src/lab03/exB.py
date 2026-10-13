from src.lib.functools import *
from sys import *


text=stdin.read()
norm_text=normalize(text)
tokens=tokenize(norm_text)
pairs=count_freq(tokens)
top5=top_n(pairs)

print(f'''
Всего слов: {len(tokens)}
Уникальных слов: {len(set(tokens))}
Топ 5: ''')
for world,count in top5:
    print(f"{world}:{count}")