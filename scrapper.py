"""
    Scrapes image data from websites        
""" 
import requests
from bs4 import BeautifulSoup

url = "https://shop.nordstrom.com/c/womens-handbags-and-wallets?origin=topnav&breadcrumb=Home%2fWomen%2fHandbags"
response = requests.get(url)

soup = BeautifulSoup(response.content, "lxml")

image_tags = soup.find_all('img')

for img in image_tags:
	print(img['src'] + "\n")