# import requests
# import json
#
# respose = requests.get('https://jsonplaceholder.typicode.com/todos')
# todos = json.loads(respose.text)
#
# # print(todos[:10])
# # print(type(todos))
#
#
# todos_by_user = {}
#
# for todo in todos:
#     if todo['completed']:
#         try:
#             todos_by_user[todo['userId']] += 1
#         except KeyError:
#             todos_by_user[todo['userId']] = 1
#
# print(todos_by_user)
#
# top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
# print(top_users)
# max_complete = top_users[0][1]
# print(max_complete)
#
# users = []
# for user, num_complete in top_users:
#     if num_complete < max_complete:
#         break
#     users.append(str(user))
#
# print(users)
#
#
# def keep(todo):
#     is_complete = todo['completed']
#     has_max_count = str(todo['userId']) in users
#     return is_complete and has_max_count
#
# with open('filtered_data_file.json', 'w') as f:
#     filered_todos = list(filter(keep, todos))
#     json.dump(filered_todos, f, indent=2)
#
# with open('filtered_data_file.json', 'r') as f:
#     data = json.load(f)
#     print(data)


# csv (Coma Separated Values) - переменные, разделенные запятыми

import csv

# with open('data.csv', 'r') as r_file:
#     file_reader = csv.reader(r_file, delimiter=';')
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f'файл содержит столбцы: {"; ".join(row)}')
#         else:
#             print(f"    {row[0]} - {row[1]}. Родился в {row[2]} году")
#             ...
#         count += 1
# print(f"всего в файле {count} строк(и)")


# with open('data.csv', 'r') as r_file:
#     field_names = ['имя', 'профессия', 'год рождения']
#     file_reader = csv.DictReader(r_file, delimiter=';', fieldnames=field_names)
#     count = 0
#     for row in file_reader:
#
#         if count == 0:
#             print(f'файл содержит столбцы: {"; ".join(row)}')
#
#         print(f"    {row['имя']} - {row['профессия']}. Родился в {row['год рождения']} году")
#
#         count += 1
# print(f"всего в файле {count} строк(и)")


# with open('student.csv', mode='w') as f:
#     writer = csv.writer(f, delimiter=';', lineterminator='\r')
#     writer.writerow(['name', 'class', 'age'])
#     writer.writerow(['женя', '9', '15'])
#     writer.writerow(['саша', '5', '12'])
#     writer.writerow(['маша', '11', '18'])

# data = [['hostname', 'vendor', 'model', 'location'],
#          ['sw1', 'Cisco', '3750', 'London, Best str'],
#          ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#          ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#          ['sw4', 'Cisco', '3650', 'London, Best str']]
#
# with open('data_sv.csv', mode='w') as f:
#     writer = csv.writer(f, delimiter=';', lineterminator='\r')
#     # for row in data:
#     #     writer.writerow(row)
#     writer.writerows(data)
#
# with open('data_sv.csv') as f:
#     print(f.read())


# with open('data_sv.csv', mode='w') as f:
#     names = ['имя', 'возраст']
#     file_writer = csv.DictWriter(f, delimiter=';', lineterminator='\r', fieldnames=names)
#     file_writer.writeheader()
#     file_writer.writerow({'имя': "саша", "возраст": "6"})
#     file_writer.writerow({'имя': "маша", "возраст": "15"})
#     file_writer.writerow({'имя': "вова", "возраст": "14"})

#
# data = [{
#     'hostname': 'sw1',
#     'location': 'London',
#     'model': '3750',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw2',
#     'location': 'Liverpool',
#     'model': '3850',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw3',
#     'location': 'Liverpool',
#     'model': '3650',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw4',
#     'location': 'London',
#     'model': '3650',
#     'vendor': 'Cisco'
# }]
#
# with open('dictwriter.csv', 'w') as f:
#     writer = csv.DictWriter(f, delimiter=';', lineterminator='\r', fieldnames=list(data[0].keys()))
#     writer.writeheader()
#     for d in data:
#         writer.writerow(d)



#парсинг

# from bs4 import BeautifulSoup
# import re
#
# # def get_copywriter(tag):
# #     whois = tag.find('div', class_='whois').text.strip()
# #     if 'Copywriter' in whois:
# #         return tag
# #     return  None
#
# def get_salary(s):
#     pattern = r'\d+'
#     res = re.search(pattern, s).group()
#     res = re.findall(pattern, s)[0]
#     print(res)
#
# f = open('index.html', encoding='utf-8').read()
# soup = BeautifulSoup(f, 'html.parser')
#
# salary = soup.find_all('div', {'data-set': 'salary'})
# for i in salary:
#     get_salary(i.text)


# copywriter = []
# row = soup.find_all('div', class_='row')
# for i in row:
#     cw = get_copywriter(i)
#     if cw:
#         copywriter.append(cw)
#
# print(copywriter)

# row = soup.find('div', class_='name').text
# row = soup.find_all('div', class_='name')
# for r in row:
#     print(r.text)
# print(row)

# row = soup.find_all('div', class_='row')[1].find('div', class_='links')
# print(row)

# row = soup.find_all('div', {'data-set': 'salary'})
# print(row)

# row = soup.find('div', string='Alena').parent.parent
# row = soup.find('div', string='Alena').find_parent(class_='row')
# print(row)

# row = soup.find('div', id='whois3').find_next_sibling()
# row = soup.find('div', id='whois3').find_previous_sibling()
# print(row)



# import requests

# r = requests.get('https://ru.wordpress.org/')
# print(r.headers)
# print(r.headers['Content-Type'])
# print(r.content)
# print(r.text)


# import requests
# from bs4 import BeautifulSoup
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     p1 = soup.find('header', id='masthead').find('p', class_='site-title').text
#     return  p1
#
# def main():
#     url = 'https://ru.wordpress.org/'
#     print(get_data(get_html(url)))
#
#
# if __name__ == '__main__':
#     main()




# import requests
# from bs4 import BeautifulSoup
# import re
# import csv
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
# def refind(s):
#     res = re.sub(r'\D+', '', s)
#     return res
#
# def write_csv(data):
#     with open('plugins.csv', 'a') as f:
#         writer = csv.writer(f, lineterminator='\r', delimiter=';')
#         writer.writerow((data['name'], data['url'], data['rating']))
#
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     p1 = soup.find_all('section', class_='plugin-section')[3]
#     plugins = p1.find_all('article')
#     # return  len(plugins)
#     for plugin in plugins:
#         name = plugin.find('h3').text
#         url = plugin.find('h3').find('a').get('href')# или .['href']
#         rating = plugin.find('span', class_='rating-count').find('a').text
#         r = refind(rating)
#         data = {'name': name, 'url': url, 'rating': r}
#         write_csv(data)


#
# def main():
#     url = 'https://ru.wordpress.org/plugins/'
#     get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()




import requests
from bs4 import BeautifulSoup
import re

def get_html(url):
    r = requests.get(url)
    return r.text

def refine_cy(s):
    return s.split()[-1]

def refine_snippet(s):
    return re.sub(r'\\U', '', s)

def write_csv(data):
    with open('plugins.csv', 'a') as f:
        writer = csv.writer(f, lineterminator='\r', delimiter=';')
        writer.writerow((data['name'], data['url'], data['snippet'], data['cy']))

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    elements = soup.find_all('article', class_='plugin-card')
    for el in elements:
        try:
            name = el.find('h3').text
        except ValueError:
            name = ''

        try:
            url = el.find('h3').find('a').get('href')
        except ValueError:
            url = ''


        try:
            snippet = el.find('div', class_='entry-excerpt').text.strip()
            snippet1 = refine_snippet(snippet)
        except ValueError:
            snippet1=''

        try:
            c = el.find('span', class_='tested-with').text.strip()
            cy = refine_cy(c)
        except ValueError:
            c=''

        data = {
            'name': name,
            'url': url,
            'snippet': snippet1,
            'cy': cy
        }
        write_csv(data)

def main():
    for i in range(12,13):
        url = f'https://ru.wordpress.org/plugins/browse/blocks/page/{i}/'
        get_data(get_html(url))

if __name__ == '__main__':
    main()

