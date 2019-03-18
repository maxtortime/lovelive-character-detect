import requests
import re

from bs4 import BeautifulSoup

URL = 'https://schoolido.lu/ajax/cards/?page={index}'

def fetch_html(index, dictionary):
    r = requests.get(url=URL.format(index=index))
    r.raise_for_status()
    dictionary = parse_html(r.content, dictionary)
    
    return dictionary

def parse_html(content, dictonary):
    html = BeautifulSoup(content, 'html.parser')
    img = html.find_all('img')
    
    for elem in img:
        if re.match(r'//i.schoolido.lu/c/\w+.\w+', elem.get('src', '')):
            try:
                dictonary[elem.get('alt', elem['src'])] = elem['src']
            except Exception as e:
                print(elem)
        
    return dictonary

idols = dict()

for i in range(1, 2):
    idols = fetch_html(i, idols)

print(idols)
