import requests
from bs4 import BeautifulSoup as bs

site=requests.get('https://stat.gov.pl/obszary-tematyczne/ceny-handel/wskazniki-cen/wskazniki-cen-towarow-i-uslug-konsumpcyjnych-pot-inflacja-/miesieczne-wskazniki-cen-towarow-i-uslug-konsumpcyjnych-od-1982-roku/')

standard_foot=0.05
money=1000
pogchmin=bs(site.content,'html.parser')
rows=pogchmin.find_all('tr')
for i in rows:
    print(i)
