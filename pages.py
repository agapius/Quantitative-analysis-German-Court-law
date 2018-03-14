# import libraries
import urllib2
from bs4 import BeautifulSoup


cray = "http://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/list.py?Gericht=bgh&Art=en&Datum=2018&Seite=100"


##just a quick function to split strings by four
def split_four(s):
    return [s[i:i+4] for i in range(0, len(s), 4)]



##create all overview pages from 2000 until 2018 (coul be optimized to directly get pages from 2000 until today)
def get_calender_years(start):
	l_start = urllib2.urlopen(start).read()
	b_start = BeautifulSoup(l_start, 'html.parser')
	r_start = b_start.html.body.table
#get the box with all the calender years - nfortunately its all in one box
	calender = r_start.findAll('div',{"id": "kaljahr"})
	calender_clean = []
#get all the years - then I have one long string with all the years- then separate after every fouth char b/c years have four digits
	for y in calender:
		y=y.get_text(strip=True).encode('utf-8')
		calender_clean.append(split_four(y))

	print(calender_clean[0])



##give it an overview page and it returns the number of pages
def get_number_of_pages(start):
#this link leads to page 100 (since there is no page 100, one is automatically redirected to the highest page)
	l_start = urllib2.urlopen(start).read()
	b_start = BeautifulSoup(l_start, 'html.parser')
	r_start = b_start.html.thead.tr
#find all page links on the last page (the last page link on the last page is the 'pre-last-page')
	pages = r_start.findAll('a',{"class": "pagelink"})
#pages[-1] gets us the number of the pre-last page. Convert this to an int to do then math with it (+1)
	Nofpages= int(pages[-1].get_text(strip=True))+1
	print(Nofpages)



##get all the downloadlinks to the Urteile and download all of them
def get_links_to_urteil(start):
	l_start = urllib2.urlopen(start).read()
	b_start = BeautifulSoup(l_start, 'html.parser')
	r_start = b_start.html.body
#find all download links to the Urteile
#would be nice to create a list of tuples with (senat,date,AKz,link)
#i'll make lists of all 4 variables and then I'll put them all together in a list as tuples

#senate
	senate = r_start.findAll('td',{"class":"ESpruchk"})
	senate_clean= []
	for s in senate:
		s= s.get_text(strip=True)
		print(s)
		senate_clean.append(s)
	print(senate_clean)

#date
	date = r_start.findAll('td',{"class":"EDatum"})
	
#downloadlinks and AkZ	
	downloadlinks = r_start.findAll('td',{"class":"EAz"})

#hier in dieser call bekomme ich die direktdownloadlinks sowie die 
#the first part of the link is always the same
	link_to_urteil1= 'http://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/'

	for d in downloadlinks:
		
		new= d.findAll('a', href=True)[1]
		link_to_urteil2= (new['href']) #da bekomme ich den link also die URL
		link_to_urteil=link_to_urteil1+link_to_urteil2
		print(link_to_urteil)
		
		aktenzeichen=(d.get_text(strip=True)) #da bekomme ich das Aktenzeichen
		print(aktenzeichen)

#sobald ich die inks habe, kann ich hier easy downloaden
'''	#f=open link to download
	f = urllib2.urlopen(bgh_pdf)
	with open("urteil.pdf", "wb") as code:
		code.write(f.read())'''


calyear = get_calender_years(cray)
nofpages = get_number_of_pages(cray)
get_links_to_urteil(cray)
#make a for loop for all calyears and in each calyear for all pages



