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
	writer.writerow(['Doknummer', 'Aktenzeichen','Gerichtstyp', 'Spruchkörper', 'Entscheidungsdatum', 'Jahr', 
		'BGH', 'BVerfG', 'LG Hamburg', 'AG Hamburg', 'OLG Hamm', 'OLG München', 'OLG Stuttgart',
		'OLG Frankfurt', 'OLG Düsseldorf', 'OLG Karlsruhe', 'OLG Dresden', 'OLG Köln', 'OLG Celle',
		'OLG Berlin', 'OLG Nürnberg', 'OLG Schleswig', 'OLG Koblenz', 'OLG Brandenburg', 'OLG Oldenburg',
		'OLG Naumburg', 'OLG Bamberg', 'OLG Jena', 'OLG Hamburg', 'OLG Rostock', 'OLG Zweibrücken',
		'OLG Braunschweig', 'OLG Saarbrücken', 'OLG Bremen', 'KG', 'OLG Saarland', 'MüKo-BGB',
		'MüKo-ZPO', 'MüKo-GmbHG', 'MüKo-InsO', 'MüKo-StGB', 'MüKo-StPO', 'MüKo-HGB', 'MüKo-AktG',
		'Sodan/Ziekow', 'Staudinger', 'Palandt', 'jurisPK-BGB', 'BeckOK-BGB', 'BeckOK-ZPO', 'BeckOK-StGB',
		'BeckOK-Datenschutzrecht', 'BeckOK-StPO', 'BeckOK-BauGB', 'BeckOK-FamFG', 'BeckOK-HGB', 'BeckOK-WEG',
		'BeckOK-UrhR', 'BeckOK-AuslR', 'BeckOK-GG', 'BeckOK-VVG', 'BeckOK-GBO', 'BeckOK-VwVfG',
		'Meyer-Goßner', 'Fischer', 'Leipziger Kommentar', 'Schönke/Schröder', 'Thomas/Putzo', 'Musielak-ZPO'
		'Zöller-ZPO', 'Baumbach-ZPO', 'Wieczorek-ZPO', 'Prütting-ZPO', 'Hk-ZPO', 'Stein/Jonas-ZPO',
		'Saenger-ZPO', 'Zimmermann-ZPO', 'Musielak-FamG', 'Baumbach-GmbH', 'Baumbach-HGB', 'Hk-InsO'])

#file = open('citations.txt', 'r+')

# we need the length to calculate the percentage done; same goes for counter 
length = len(xmllist)
count = 0
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
	jahr= int(str(entschdatum)[0:4])
	aktenzeichen= root.find('aktenzeichen').text
	doktyp= root.find('doktyp').text
	##get the citations 
	doknrlist = []
	for p in root.iter('p'):
		if bool(p.text):
		###scan the paragraph with re for possible citations
			list_of_citations = scan_paragraph(p.text)
			for quote in list_of_citations:
				found_source = find_source(quote)
				if(found_source):
					doknrlist.append(found_source) 
			
		###add citations with doknrlist.append(citations)	
	# listcount gibt immer die Anzahl an gefundenen Zitaten zurück (und löscht dann diese Einträge), wenn nichts gefunden wird, dann gibt es 0 zurück.
	BGH = listcount(doknrlist, 'BGH')
	BVerfG = listcount(doknrlist, 'BVerfG')
	LG_Hamburg = listcount(doknrlist, 'LG Hamburg')
	AG_Hamburg = listcount(doknrlist, 'AG Hamburg')
	OLG_Hamm = listcount(doknrlist, 'OLG Hamm')
	OLG_München = listcount(doknrlist, 'OLG München')
	OLG_Stuttgart = listcount(doknrlist, 'OLG Stuttgart')
	OLG_Frankfurt = listcount(doknrlist, 'OLG Frankfurt')
	OLG_Karlsruhe = listcount(doknrlist, 'OLG Karlsruhe')
	OLG_Dresden = listcount(doknrlist, 'OLG Dresden')
	OLG_Köln = listcount(doknrlist, 'OLG Köln')
	OLG_Celle = listcount(doknrlist, 'OLG Celle')
	OLG_Berlin = listcount(doknrlist, 'OLG Berlin')
	OLG_Nürnberg = listcount(doknrlist, 'OLG Nürnberg')
	OLG_Schleswig = listcount(doknrlist, 'OLG Schleswig')
	OLG_Brandenburg = listcount(doknrlist, 'OLG Brandenburg')
	OLG_Oldenburg = listcount(doknrlist, 'OLG Oldenburg')
	OLG_Naumburg = listcount(doknrlist, 'OLG Naumburg')
	OLG_Bamberg = listcount(doknrlist, 'OLG Bamberg')
	OLG_Jena = listcount(doknrlist, 'OLG Jena')
	OLG_Hamburg = listcount(doknrlist, 'OLG Hamburg')
	OLG_Rostock = listcount(doknrlist, 'OLG Rostock')
	OLG_Zweibrücken = listcount(doknrlist, 'OLG Zweibrücken')
	OLG_Braunschweig = listcount(doknrlist, 'OLG Braunschweig')
	OLG_Saarbrücken = listcount(doknrlist, 'OLG Saarbrücken')
	KG = listcount(doknrlist, 'KG')
	OLG_Saarland = listcount(doknrlist, 'OLG Saarland')
	MüKo-BGB = listcount(doknrlist, 'MüKo-BGB')



	writer.writerow([doknr, aktenzeichen, gertyp, spruchkoerper, entschdatum, jahr, BGH, BVerfG, LG_Hamburg, AG_Hamburg, 
		OLG_Hamm, OLG_München, OLG_Stuttgart,
		OLG_Frankfurt, OLG_Düsseldorf, OLG_Karlsruhe, OLG_Dresden, OLG_Köln, OLG_Celle,
		OLG_Berlin, OLG_Nürnberg, OLG_Schleswig, OLG_Koblenz, OLG_Brandenburg, OLG_Oldenburg,
		OLG_Naumburg, OLG_Bamberg, OLG_Jena, OLG_Hamburg, OLG_Rostock, OLG_Zweibrücken,
		OLG_Braunschweig, OLG_Saarbrücken, OLG_Bremen, KG, OLG_Saarland, MüKo-BGB,
		'MüKo-ZPO', 'MüKo-GmbHG', 'MüKo-InsO', 'MüKo-StGB', 'MüKo-StPO', 'MüKo-HGB', 'MüKo-AktG',
		'Sodan/Ziekow', 'Staudinger', 'Palandt', 'jurisPK-BGB', 'BeckOK-BGB', 'BeckOK-ZPO', 'BeckOK-StGB',
		'BeckOK-Datenschutzrecht', 'BeckOK-StPO', 'BeckOK-BauGB', 'BeckOK-FamFG', 'BeckOK-HGB', 'BeckOK-WEG',
		'BeckOK-UrhR', 'BeckOK-AuslR', 'BeckOK-GG', 'BeckOK-VVG', 'BeckOK-GBO', 'BeckOK-VwVfG',
		'Meyer-Goßner', 'Fischer', 'Leipziger Kommentar', 'Schönke/Schröder', 'Thomas/Putzo', 'Musielak-ZPO'
		'Zöller-ZPO', 'Baumbach-ZPO', 'Wieczorek-ZPO', 'Prütting-ZPO', 'Hk-ZPO', 'Stein/Jonas-ZPO',
		'Saenger-ZPO', 'Zimmermann-ZPO', 'Musielak-FamG', 'Baumbach-GmbH', 'Baumbach-HGB', 'Hk-InsO'])
	print('Sucess:' + str(xml))
	count += 1
	#prints out the percentage of files already parsed and included in xml
	print_percentage(count, length)
file.close()
print('Done')
	