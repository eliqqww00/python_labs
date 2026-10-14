from src.lib.functools import read_text, write_csv
from src.lib.functools import normalize,tokenize,count_freq,top_n

text=read_text("data/lab04/input.txt")


words=tokenize(normalize(text))
counts=count_freq(words)
top_5=top_n(counts)

rows=sorted(counts.items(), key=lambda w: (-w[1],w[0]))
write_csv(rows,"data/lab04/report.csv",['word','count'])

print(f'''
Всего слов: {len(words)}
Уникальных слов: {len(set(words))}
Топ-5: ''')
for word,count in top_5:
    print(f'{word}:{count}')