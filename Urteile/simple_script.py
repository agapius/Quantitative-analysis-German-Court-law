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



'''<item>
<gericht>BGH 9. Zivilsenat</gericht>
<entsch-datum>20100114</entsch-datum>
<aktenzeichen>IX ZB 72/08</aktenzeichen>
<link>http://www.rechtsprechung-im-internet.de/jportal/docs/bsjrs/JURE100055033.zip</link>
<modified>2016-01-25T22:46:20Z</modified>
</item>
'''



