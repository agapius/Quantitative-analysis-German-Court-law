#Analytics
import os
import csv
import re
import xml.etree.ElementTree as ET
from regex import *

#create a list of all files in directory
xmllist= []
for file in os.listdir():
    if file.endswith(".xml"):
        xmllist.append(file)


#open the megasheet.csv and create the headers
with open('megasheet.csv', 'w') as csvfile:
	writer = csv.writer(csvfile, delimiter=',')
	writer.writerow(['Doknummer', 'Aktenzeichen','Gerichtstyp', 'Spruchkörper', 'Entscheidungsdatum', 'Zitat(Kommentar)', 'Zitat(Entscheidung)', 'Zitat(Autor)'])

file = open('citations.txt', 'r+')

##loop through all xml files in the diectory
for xml in xmllist:
	#get data from xml general
	tree = ET.parse(xml)
	root = tree.getroot()
	##get specific data tags
	doknr= root.find('doknr').text
	gertyp= root.find('gertyp').text
	spruchkoerper= root.find('spruchkoerper').text
	entschdatum= root.find('entsch-datum').text
	aktenzeichen= root.find('aktenzeichen').text
	doktyp= root.find('doktyp').text
	##get the citations 
	doknrlist = []
	for p in root.iter('p'):
		if bool(p.text):
		###scan the paragraph with re for possible citations
			doknrlist = doknrlist + scan_paragraph(p.text)
			
		###add citations with doknrlist.append(citations)	
	# listcount gibt immer die Anzahl an gefundenen Zitaten zurück (und löscht dann diese Einträge), wenn nichts gefunden wird, dann gibt es 0 zurück.
	NStZ = listcount(doknrlist, 'NStZ')
	Palandt = listcount(doknrlist, 'Palandt')
	...
	writer.writerow([doknr, aktenzeichen, gertyp, spruchkoerper, entschdatum, 'Zitat(Kommentar)', 'Zitat(Entscheidung)', 'Zitat(Autor)'])
	print('Sucess:' + str(xml))
file.close()
print('Done')
	