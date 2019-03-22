import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
import datetime

url = "http://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/list.py?Gericht=bgh&Art=en&Datum="
base_url = "http://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/"
failed_downloads = []
count = 0

#returns no_pages as int 
def get_number_of_pages(url_year):
	website = urllib.request.urlopen(url_year).read()
	soup = BeautifulSoup(website, 'html.parser')
	no_pages = int(soup.find(onmouseover="window.document.images['img_p_rright'].src='/rechtsprechung/bgh/images/p_rright_h.gif'").attrs['href'].rsplit('=',1)[1])
	return no_pages

#returns list of url's for all pages from a year
def get_pages_url(year):
	url_list = []
	url_year = url + year
	no_pages = get_number_of_pages(url_year)
	for page in range(no_pages):
		url_list.append(year+"&Seite="+str(page))
	return url_list

#returns list of url's for all pages since 2000
def get_all_pages_url():
	url_list = []
	year_current = datetime.datetime.now().year
	for year in range(2000,year_current):
		url_list.append(get_pages(year))
	return url_list

#returns list of (Az, url.pdf) of decisions from a page
def get_decisions(page_url):
	url_list = []
	soup = BeautifulSoup(urllib.request.urlopen(page_url), 'html.parser')
	doklinks = soup.find_all("a","doklink")
	for dok in doklinks:
		decision_title = dok.string
		decision_pdf = base_url + dok.attrs['href'] + "&Blank=1.pdf"
		url_list.append((decision_title, decision_pdf))
	return url_list

#downloads a decision 
def download_decision(pdf_url):
	try:
		filename = pdf[0]
		pdf_link = urllib.request.urlopen(pdf[1])
		with open(filename, 'wb') as out:
			out.write(pdf_link.read())
	except urllib.error.URLError as j:
		print('Failed opening page: {}'.format(pdf_link))
		failed_downloads.append(pdf_url)

def print_failed_downloads():
	if not failed_downloads:
		print('No failed downloads')
	else:
		print('Failed downloads:')
		print(failed_downloads)

def download_decisions(url_list):
	for url in url_list:
		total_pages = len(url_list)
		count += 1
		try:
			decisions = get_decisions(url)
			for pdf in decisions:
				download_decision(pdf_url)
		except urllib.error.URLError as l:
			print('Failed opening page:' + str(url))
		print("Page {} out of {} is done.".format(count, total_pages))
	print('Downloads completed')
