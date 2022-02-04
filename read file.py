file = open('folder with texts/text.txt', 'r', encoding='utf-8')  # otwórz plik (nazwa pliku, uprawnienia- domyślnie read)
#  open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True)

# file = open('text.txt', 'w')  # jeśli otworzyć z uprawnieniami write to plik się wyczyści
# f = file.read()
f_lines = file.readlines()
print(file)
print(f_lines)

new_list = []
for line in f_lines[:-1]:
    new_list.append(line.strip())

print(new_list)

file.close()
