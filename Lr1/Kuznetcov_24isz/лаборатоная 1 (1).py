alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
word = input()
print(' '.join(str(alphabet.index(c) + 1) for c in word))