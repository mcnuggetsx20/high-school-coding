from bs4 import BeautifulSoup
import requests as rq
import scan

url = 'https://www.flickr.com/photos/cameralabs/with/12382975864/'

page = rq.get(url).content

soup = BeautifulSoup(page, 'html.parser')
imgs = soup.findAll("a")
print(imgs)

