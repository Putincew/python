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