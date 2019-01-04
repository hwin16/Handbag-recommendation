"""
    Scrapes image data from websites        
""" 
import urllib.request
from bs4 import BeautifulSoup

url = "https://shop.nordstrom.com/c/womens-handbags-and-wallets?origin=topnav&breadcrumb=Home%2fWomen%2fHandbags"
response = urllib.request.urlopen(url)

soup = BeautifulSoup(response, "lxml")

image_tags = soup.find_all('img')

for img in image_tags:
	pic_link = img['src']
	pic_name = pic_link[:pic_link.index('?')]
	pic_name = pic_name.split('/')[-1]

	print(pic_link, pic_name)
	filename, headers = urllib.request.urlretrieve(pic_link, 'data/' + pic_name)

	print(filename)