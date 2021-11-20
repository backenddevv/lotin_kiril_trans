from transliterate import to_latin, to_cyrillic
matn = input("Matn kiriting: ")

if matn.isascii():
    print(to_cyrillic(matn))
else:
    print(to_latin(matn))
