def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:

    if casefold:
        text=text.casefold()
    else:
        text=text.lower()

    if yo2e==True:
        text=text.replace('Ё','Е')
        text=text.replace('ё','е')

    text=' '.join(text.split())
    return text

print(normalize('йййй\tй'))