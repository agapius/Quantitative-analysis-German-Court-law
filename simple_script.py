import requests
from bs4 import BeautifulSoup

xml = requests.get('https://www.rechtsprechung-im-internet.de/rii-toc.xml')

soup = BeautifulSoup(xml.text, 'xml')

failed_downloads= []

for item in soup.find_all('item'):
	current_item = item
	zip_link = current_item.link.text
	name1 = current_item.gericht.text
	name2 = current_item.aktenzeichen.text
	name_final = name1+'_'+name2

	print(zip_link)
	print(type(zip_link))
	print(name_final)

print("We found %d Urteile im XML Format" %(len(soup.find_all('link')))