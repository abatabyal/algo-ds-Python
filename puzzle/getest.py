import requests
import json

url = 'https://jsonmock.hackerrank.com/api/movies/search/?Title=spiderman&page=1'

r = requests.get(url=url)
r = r.json()
nos_pages = r['total_pages']
titles = []

for t in r['data']:
    titles.append(t['Title'])

for i in range(2, nos_pages + 1):
    url_t = 'https://jsonmock.hackerrank.com/api/movies/search/?Title=spiderman&page=' + str(i)
    r = requests.get(url=url_t)
    r = r.json()
    for t in r['data']:
        titles.append(t['Title'])

titles.sort()
print(titles)