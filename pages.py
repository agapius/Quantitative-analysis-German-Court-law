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



get_number_of_pages(cray)
get_calender_years(cray)