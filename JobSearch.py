import requests
from bs4 import BeautifulSoup
import pandas as pd


def extract(page):
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/112.0.0.0 Safari/537.36 OPR/98.0.0.0'}
    url1 = 'https://fr.jooble.org/SearchResult?p=5&ukw=data%20scientist'
    r = requests.get(url1, headers)
    print(r.status_code)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup


Joblist = []


def transform(soup):
    divs = soup.find_all('article', class_='FxQpvm yKsady')
    # divs= soup.find_all('div', class_ = 'cardOutline')
    # print(len(divs))
    for item in divs:
        title = item.find('a').text.strip()
        company = item.find('p', class_='Ya0gV9').text.strip()
        try:
            salary = item.find('p', class_='jNebTl').text.strip()
        except:
            salary = ''
        summary = item.find('div', class_='_9jGwm1').text.strip().replace('\n', '')
        job = {
            'title': title,
            'company': company,
            'salary': salary,
            'summary': summary
        }
        Joblist.append(job)
    return


def extract1(page):
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/112.0.0.0 Safari/537.36 OPR/98.0.0.0'}
    url = f'https://www.keejob.com/offres-emploi/?page={page}'
    q = requests.get(url, headers)
    print(q.status_code)
    soup1 = BeautifulSoup(q.content, 'html.parser')
    return soup1


def transform1(soup1):
    divs = soup1.find_all('div', class_='block_white_a post clearfix premium-job-block')
    for item in divs:
        title = item.find('h6').text.strip()
        company = item.find('div', class_='span11 no-margin-left').text.strip()
        summary = item.find('p').text.strip()
        job1 = {
            'title': title,
            'company': company,
            'summary': summary
        }
        Joblist.append(job1)
    return


def extract2(page):
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/112.0.0.0 Safari/537.36 OPR/98.0.0.0'}
    url2 = f'https://www.optioncarriere.tn/emplois-tunisie-123097.html?p={page}'
    s = requests.get(url2, headers)
    print(s.status_code)
    soup2 = BeautifulSoup(s.content, 'html.parser')
    return soup2


def transform2(soup2):
    divs = soup2.find_all('article', class_='job clicky')
    for item in divs:
        title = item.find('a').text.strip()
        company = item.find('p', class_='company').text.strip()
        location = item.find('ul', class_='location').text.strip()
        summary = item.find('div', class_='desc').text.strip().replace('\n', '')
        job2 = {
            'title': title,
            'company': company,
            'location': location,
            'summary': summary
        }
        Joblist.append(job2)
    return


for i in range(0, 40, 10):
    #il faut commencer par page = 1
    c = extract1(1)
    x = extract2(0)
    transform2(x)

df = pd.DataFrame(Joblist)
df.sort_values(by='title')
df.nsmallest(70,'summary')
print(df.head())

df.to_csv('job.csv')
