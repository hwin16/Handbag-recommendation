"""
    Scrapes image data from websites        
""" 

from bs4 import BeautifulSoup

with open("data/bags.htm") as fp:
	soup = BeautifulSoup(fp, "lxml")

image_tags = soup.find_all('img')

for img in image_tags:
	print(img['src'] + "\n")