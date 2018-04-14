import requests
from bs4 import BeautifulSoup
xml = requests.get('https://www.rechtsprechung-im-internet.de/rii-toc.xml')
soup = BeautifulSoup(xml.text, 'xml')
counter=0

for item in soup.find_all('item'):
	ziplink=str(item.link.text) 
	datum=str(item.find('entsch-datum').text)
	az=str(item.aktenzeichen.text)
	hof=str(item.gericht.text)
	if ziplink.find('/'):
		name = ziplink.rsplit('/',1)[1]
	r=requests.get(ziplink, allow_redirects=True)
	with open('%s' % name,'wb') as f:
		f.write(r.content)
	print(name)
	counter=counter+1
	print(counter)
	
#still needs some status updates during the scan - maybe a percentage
#still needs error-handling
