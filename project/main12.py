import os
import time

print(os.path.exists(r'C:\python_learn\python\project\test.txt')) # проверяет наличие файла по указанному пути
path = 'test.txt'
print(os.path.getatime(path)) # время последнего доступа к файлу в секундах
print(os.path.getctime(path)) # время создания
print(os.path.getmtime(path)) # время последнего изменения
print(os.path.getsize(path)) # размер файла в байтах

size = round(os.path.getsize(path) / 1024, 2)
print(size)

t = os.path.getctime(path)
print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(t)))

print(os.path.isfile(r'C:\python_learn\python\project\test.txt'))
print(os.path.isdir(r'C:\python_learn\python\project\test.txt'))












