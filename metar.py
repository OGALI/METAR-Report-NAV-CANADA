import requests, bs4, sys, webbrowser


url = 'https://flightplanning.navcanada.ca/cgi-bin/Fore-obs/metar.cgi?NoSession=NS_Inconnu&format=raw&Langue=anglais&Region=can&Stations='
if len(sys.argv) > 1:
    airport = sys.argv[1]
else:
    airport = input('Enter the code for the airport: ')

full_url = url + airport
res = requests.get(full_url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text)
metarList = soup.select('b div')

for tag in metarList:
    print(tag.getText())

