open('text1.txt', 'w').write('Первый файл. ')
open('text2.txt', 'w').write('Второй файл. ')
open('text3.txt', 'w').write(open('text1.txt', 'r').read() + open('text2.txt', 'r').read())










