import requests
from bs4 import BeautifulSoup
import pandas as pd


def extract(page):
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 OPR/98.0.0.0'}
    url = f'https://www.indeed.com/jobs?q=data+scientist&l=Florida&radius=35&start={page}'
    url1 = 'https://fr.jooble.org/SearchResult?p=5&ukw=data%20scientist'
    r = requests.get(url1, headers)
    print(r.status_code)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

joblist = []


def transform(soup):
    divs= soup.find_all('article', class_='FxQpvm yKsady')
    #divs= soup.find_all('div', class_ = 'cardOutline')
    print(len(divs))
    for item in divs:
        title = item.find('a').text.strip()
        company = item.find('p' , class_ = 'Ya0gV9').text.strip()
        try:
            salary = item.find('p' , class_ = 'jNebTl').text.strip()
        except:
            salary= ''
        summary = item.find('div' , class_ = '_9jGwm1').text.strip().replace('\n','')
        job = {
            'title' : title,
            'company' : company,
            'salary' : salary,
            'summary' : summary
        }
        joblist.append(job)
    return

for i in range(0,40,10):
    c = extract(0)
    transform(c)

df = pd.DataFrame(joblist)

print(df.head())

df.to_csv('job.csv')

