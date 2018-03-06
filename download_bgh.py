# import libraries
import urllib2

bgh_urteil_link= "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bgh&Art=en&Datum=Aktuell&nr=81405&pos=11&anz=516"

p = urllib2.urlopen(bgh_urteil_link)


#create a variable with the link to the urteil
bgh_pdf = "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bgh&Art=en&Datum=Aktuell&nr=81405&anz=516&pos=11&Frame=4&.pdf"

# query the website and return the html to the variable 



f = urllib2.urlopen(bgh_pdf)
with open("Urteil.pdf", "wb") as code:
	code.write(f.read())