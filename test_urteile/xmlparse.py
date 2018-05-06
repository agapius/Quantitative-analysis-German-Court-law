#Analytics
from os import listdir
import csv
import re
import xml.etree.ElementTree as ET

#create a list of all files in directory
xmllist= os.listdir()

with open('megasheet.csv', 'wb') as csvfile:
	writer = csv.writer(csvfile, delimiter=',')
	writer.writerow(['Doknummer', 'Aktenzeichen','Gerichtstyp', 'Spruchkörper', 'Entscheidungsdatum', 'Zitat(Kommentar)', 'Zitat(Entscheidung)', 'Zitat(Autor)'])

	for xml in xmllist:
		#get data from xml
		tree = ET.parse('xml')
		root = tree.getroot()

		##get simple tags
		doknr= root.find('doknr').text
		gertyp= root.find('gertyp').text
		spruchkoerper= root.find('spruchkoerper').text
		entschdatum= root.find('entsch-datum').text
		aktenzeichen= root.find('aktenzeichen').text
		doktyp= root.find('doktyp').text

		'''##gets all the text from the decision
								for p in root.iter('p'):
									if bool(p.text):
									###scan the paragraph with re for possible citations
									###add citations with doknrlist.append(citations)
									print(p.text)'''



'''pattern = "\(.*?(NJW).*?\)

with 
for match in re.findall(pattern, text):'''



		writer.writerow([doknr, aktenzeichen, gertyp, spruchkoerper, entschdatum, 'Zitat(Kommentar)', 'Zitat(Entscheidung)', 'Zitat(Autor)'])
		