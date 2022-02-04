file_read = open('folder with texts/text.txt', 'r', encoding='utf-8')
x = file_read.read()
file_read.close()


file_write = open('python_file.txt', 'w', encoding='utf-8')
file_write.write(x)
print(x)
file_read_lines = x.split('\n')

for line in file_read_lines:
    file_write.write(line[:-1])

print('done')
file_write.close()
