# работа с файлами

# f = open('C:\\python_learn\\python\\project\\text.txt', 'r')
# print(f)
# print(*f)
# print(f.closed)
# f.close()
# print(f.closed)
# print(f.mode)
# print(f.name)
# print(f.encoding)
#
# f = open('text.txt', 'r')
# print(f.read(3))
# print(f.read())
# f.close()

# f = open('text.txt', 'r')
# try:
#     print(f.read())
# finally:
#     f.close()
#
# f = open('test.txt', 'r')
# print(f.readline())
# print(f.readline(8))
# print(f.readline())
# print(f.readline())

# f = open('test.txt', 'r')
# print(f.readlines())
# f.close()


# f = open('test.txt', 'r')
# for line in f:
#     print(line)
# f.close()



# f = open('test.txt', 'r')
# print(len(f.readlines()))
# f.close()

# f = open('xyz.txt', 'w')
# f.write('привет\nworld!')
# # f.write(str(5))
# f.close()
#
# f = open('xyz.txt', 'a')
# f.write('\nновый текст')
# # print(f.write('\nновый текст'))
# # f.write(str(5))
# Lines = ['\nлиния 1', '\nлиния2']
# f.writelines(Lines)
# f.close()

# f = open('xyz.txt', 'w')
# lst = [str(i)+str(i-1)+'\t' for i in range(1, 20)]
# print(lst)
# # f.writelines(lst)
# f.close()

# f = open('text2.txt', 'w')
# f.write('замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл')
# f.close()
#
# f = open('text2.txt', 'r')
# read_file = f.readlines()
# print(read_file)
# for i in range(len(read_file)):
#     if read_file[i] == 'изменить строку в списке;\n':
#         read_file[i] = 'hello world\n'
# f.close()
#
# f = open('text2.txt', 'w')
# f.writelines(read_file)
# f.close()
#
# f = open('text2.txt', 'w')
# f.write('замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл')
# f.close()

# f = open('text.txt', 'r')
# print(f.read(3))
# print(f.tell())
# print(f.seek(1))
# print(f.read())
# print(f.tell())
# f.close()

# f = open('text.txt', 'r+')
# print(f.write('i am learning python'))
# print(f.seek(3))
# print(f.write('--new string--'))
# print(f.tell())
# f.close()

# f = open('text.txt', 'wb')
# print(f.write(b'i am learning python'))
# # print(f.seek(3))
# # print(f.write('--new string--'))
# # print(f.tell())
# f.close()

f = open('dz.txt', 'w')
f.write('Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n')
f.close()
f = open('dz.txt', 'r')
str = f.readlines()
a = int(input('1-й индекс строки для замены: '))
b = int(input('2-й индекс строки для замены: '))
if a > len(str)-1 or b > len(str)-1:
    print('строки с таким индексом нет')
    f.close()
else:
    str[a], str[b] = str[b], str[a]
    print(str)
    f.close()
    f = open('dz.txt', 'w')
    f.writelines(str)
    f.close()



