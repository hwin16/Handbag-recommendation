"""
    Scrapes image data from websites        
""" 
import os
import requests
import urllib.request
from bs4 import *

page_number = 1
product_count = -1 # if there is no item available for the link, this will be set to 0
downloaded_count = 0

while product_count > downloaded_count or product_count==-1:
	print (page_number)
	url = "https://www.macys.com/shop/handbags-accessories/handbags/Pageindex/{}?id=27686".format(page_number)
	hdr = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
	session = requests.Session() # this is used instead of urllib to avoid 403 forbidden error
	response = session.get(url, headers = hdr)
	
	soup = BeautifulSoup(response.content, "lxml")
	
	if product_count == -1:
		div_tags = soup.find_all('span')
		for div in div_tags:
			if div.has_attr('id'):
				if 'productCount' in div['id']:
					product_count = int( str(div.string) ) # html gives NavigableString object

	# path = 'data/page' + str(page_number) + '/'
	# if not os.path.exists(path):
	# 	os.makedirs(path)

	image_tags = soup.find_all('img')
	for img in image_tags:
		pic_link = img['src']
		if '?' in pic_link:
			pic_name = pic_link[:pic_link.index('?')]
		else:
			pic_name=pic_link
		pic_name = pic_name.split('/')[-1]

		# download pic
		try:
			filename, headers = urllib.request.urlretrieve(pic_link, 'data/' + pic_name)
			downloaded_count += 1
			print("download " + str(downloaded_count) + ": " + filename)
		except:
			print("can't download", pic_link)
			pass

	page_number += 1
