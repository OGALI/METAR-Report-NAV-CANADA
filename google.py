import requests
import bs4
import sys
import webbrowser

print('Googling...')

res = requests.get('https://www.google.ca/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text)
print('Download complete.')
linkElem = soup.select('.r a')

numOpen = min(5, len(linkElem))


links = ['http://google.com' + i.get('href') for i in linkElem]
print(links)
