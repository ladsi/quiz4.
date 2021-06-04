import requests
from bs4 import BeautifulSoup
import csv
from time import sleep

file = open('wignebi.csv', 'w', encoding='UTF-8_sig')
#file.write('სათაური,ავტორი\n')
file_csv = csv.writer(file)
file_csv.writerow(['Title','Author'])
url_p = {'page':'books', '[page]' : 1}
while True:
    url = 'https://www.lit.ge/index.php?page=books&send[shop.catalog][page]='
    r = requests.get(url, params=url_p)
    print(r)
    content = r.text
    soup = BeautifulSoup(content, 'html.parser')
    section = soup.find('section', {'class':'list-holder'})
    all_book = section.find_all('article', {'class':'item-holder'})
    for each in all_book:
        title = each.find('div', {'class': 'title-bar'})
        title_b = title.a.text
        author = title.b.a.text
        print(author)
        #file.write(title_b+','+author+'\n')
        file_csv.writerow([title_b,author])
    url_p['[page]'] += 1
    sleep(16)
