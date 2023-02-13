import requests
from bs4 import BeautifulSoup
import csv

def get_html(url):
    r = requests.get(url)
    return r.text

def write_csv(data):
    with open('table.csv', 'a') as f:
        writer = csv.writer(f, lineterminator='\r', delimiter=';')
        if data['thems']:
            writer.writerow((data['thems'], data['link']))

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    news = soup.find('div', class_='l-base__flex l-base__flex__gutter l-base__flex__content item-list js-load-container').find_all('a')

    for i in news:
        try:
            txt = i.text.strip()
        except Exception:
            txt = 'no text'

        try:
            link = i.get('href')
        except Exception:
            link = 'no link'

        data = {
            'thems': txt,
            'link': link
        }

        write_csv(data)

def main():
    url = 'https://trends.rbc.ru/trends/tag/educational_startups'
    get_data(get_html(url))

if __name__ == '__main__':
    main()