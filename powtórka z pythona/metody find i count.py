str1 = 'hello'
print(str1.find('ll'))  # -> return 2 bo znalazł zadany ciąg znaków w indeksie 2
# jeśli nie ma zadanej frazy to zwraca -1

print(str1.count('ll'))  # return 1 bo znalazł 1 frazę ll w hello
# jeśli nie ma zadanej frazy to zwraca -1

str2 = 'helllo'
print(str2.count('ll'))  # return 1 bo znalazł 1 frazę ll w hello
# dziwne że nie zwrócił 2. Wygląda to tak jakby robił drop dla frazy i dlatego zwrócił 1 a nie 2


"""
# program który zwraca liste z numerami indeksów gdzie znalazł dany znak
np jest słowo 'baba jaga' return: [1, 3, 6, 8]
"""
my_word = 'baba jaga'


def return_indexes_of_letter(word, letter):
    list_of_indexes = []
    for i, ch in enumerate(word):
        if ch == letter:
            list_of_indexes.append(i)
    return list_of_indexes


x = return_indexes_of_letter(my_word, 'a')
print(x)


y = [i for i, ch in enumerate(my_word) if ch == 'a']  # to co powyżej tylko w 1 linijce
print(y)
