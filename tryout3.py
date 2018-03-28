# import libraries
import urllib.request
from bs4 import BeautifulSoup
import re

def remove_non_ascii_1(text):
	new_string = ''.join(i for i in text if ord(i)<128)
	new_string = new_string.replace('.', ' ')
	return new_string.replace('/', ' ')


url="http://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bgh&Art=en&Datum=Aktuell&Sort=12288&Seite=0&nr=82119&pos=0&anz=542"





name = urllib.request.urlopen(url)
soup_name = BeautifulSoup(name, 'html.parser')

print(soup_name.title.string)
name_box = remove_non_ascii_1(soup_name.title.string)
print(name_box)

