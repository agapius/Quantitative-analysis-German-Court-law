#Analytics
import os
import csv
import re
import xml.etree.ElementTree as ET

#create a list of all files in directory
xmllist= []
for file in os.listdir():
    if file.endswith(".xml"):
        xmllist.append(file)
print(xmllist)
with open('megasheet.csv', 'w') as csvfile:
	writer = csv.writer(csvfile, delimiter=',')
	writer.writerow(['Doknummer', 'Aktenzeichen','Gerichtstyp', 'Spruchkörper', 'Entscheidungsdatum', 'Zitat(Kommentar)', 'Zitat(Entscheidung)', 'Zitat(Autor)'])

	for xml in xmllist:
		#get data from xml
		tree = ET.parse(xml)
		root = tree.getroot()

		##get simple tags
		doknr= root.find('doknr').text
		gertyp= root.find('gertyp').text
		spruchkoerper= root.find('spruchkoerper').text
		entschdatum= root.find('entsch-datum').text
		aktenzeichen= root.find('aktenzeichen').text
		doktyp= root.find('doktyp').text
		writer.writerow([doknr, aktenzeichen, gertyp, spruchkoerper, entschdatum, 'Zitat(Kommentar)', 'Zitat(Entscheidung)', 'Zitat(Autor)'])
		