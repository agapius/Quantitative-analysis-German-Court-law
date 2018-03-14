##treasurehunt

# import libraries
import urllib2
import datetime
from bs4 import BeautifulSoup

#functions:

##give it an overview page and it returns the number of pages
def get_number_of_pages(start):
###this link leads to page 100 (since there is no page 100, one is automatically redirected to the highest page)
	l_start = urllib2.urlopen(start).read()
	b_start = BeautifulSoup(l_start, 'html.parser')
	r_start = b_start.html.thead.tr
###find all page links on the last page (the last page link on the last page is the 'pre-last-page')
	pages = r_start.findAll('a',{"class": "pagelink"})
###pages is a list of tags. the for-loop iterates trough the tags, converts them to a string, and then returns a number, which is the page of the previous pages
	Nofpages= int(pages[-1].get_text(strip=True))+1
	print Nofpages
	return Nofpages

#Outer loop that goes through the Years

##get a list of years that we can loop throuh:

###set first year
year= 2000
now = datetime.datetime.now()
print now.year



url_year="http://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/list.py?Gericht=bgh&Art=en&Datum="
list_of_year_page_url= []
###loop through all years until now and concatenate a relevant link with the year_url
while year <= now.year:
	url_year="http://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/list.py?Gericht=bgh&Art=en&Datum="+str(year)
	page=0
	nofpages=get_number_of_pages(url_year+'&Seite=100')
	while page <= nofpages:
		url_year_pages= url_year+"&Seite="+str(page)
		list_of_year_page_url.append(url_year_pages)
		page += 1
	year += 1
###result is a list of all the pages in every year from 2000-2018

for url in list_of_year_page_url:
	print url

##loop through the urls is outmost loop

