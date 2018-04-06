# import libraries
import urllib.request, urllib.error, urllib.parse
import datetime
from bs4 import BeautifulSoup

#Get all pages URL's
	## append them to a list
#print len(list with all page urls)
#check if len(list with all pages URL's) == 14757/25
#print results

#for page in list with all pages
	##per page:
	###find docID and concatenate with URL
	###append all concatenated docID's to dictionary: Page:List of URL's (maybe this and the tep before in one line?)
	###remove doubles bei den doc.id's
	###print page
	###print len(list of URL's)
	###append error if list of URL is < 25 to errorList

#for page in dictionary  
	##print(page)
	##for URL in dictionary
	##print counter (from one to 25)
	##download URL
	##error handling: add url to list of url errors if no response

