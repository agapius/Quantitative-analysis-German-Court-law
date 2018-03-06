# import libraries
import urllib2
from bs4 import BeautifulSoup
import re

##For all overview Pages (Year, Month)
#for loop through every year/month

##Specific overview page 
#for loop through all pages of the current year (pages begin with 0)

#get senat, date, AZ and link to the bgh_urteil_link (pdf link can be extracted from there)
bgh_urteil_link= "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bgh&Art=en&Datum=Aktuell&nr=81405&pos=11&anz=516"

p = urllib2.urlopen(bgh_urteil_link)
soup = BeautifulSoup(p, 'html.parser')
#gets title tag
name_box = soup.find("title")
#gets only the text from the title tag
clean_name_urteil= name_box.get_text(strip=True)
#prints the name of the Urteil
print(clean_name_urteil)



##Download the Urteil and save it with the appropriate name
#create a variable with the link to the urteil
bgh_pdf = "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bgh&Art=en&Datum=Aktuell&nr=81405&anz=516&pos=11&Frame=4&.pdf"

#f=open link to download
f = urllib2.urlopen(bgh_pdf)
with open("%s.pdf" %clean_name_urteil, "wb") as code:
	code.write(f.read())
