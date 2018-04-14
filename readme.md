# Access Rechtsprechung-im-Internet
## Get all 14k XML Files BGH - DONE
## Get rest of XML Files -DONE
## XML
	1. Unzip all (Ignore Pictures) -> full of xml
	unzip backslash*.zip -d targetdirectory (how to extract only xml?)
	2. Go through *.xml and get list of all BGH-AZ und datum (count & compare to BGH since 2000)
	3. Find out what "<dl><dt><dd>" stand for. 
## XML to JSon
	1. Additional Tagging (most difficult)
		* Zitate mit Regex 
		* Entscheidungsträger (immer letzter/vorletzter Absatz?)
	2. Conversion
		* Standart-Converter from the internet?
		* Build custom?
			* for xml-class in XML create JSon Class
			* maybe to Excel custom and then from Excel to JSon easy thus standart is ok
## JSon -> Mongo 
	1. should be super easy:
	2. "mongoimport --db Urteile --collection BGH/BVerwG,... --drop --file ~/documents/backslash*.json"
## Query
	1. "Most cited author/Kommentar?"; "# of decisions(/decisions per judge"; "most §'s subject to debate"
	2. Query decisions by keywords, connections, judges
	3. Query using sentiment analysis and other kinds of more creative analysis
	4. "Andere kauften auch"-Option (was haben sich andere angeschaut, die dieses Urteil angesehen haben)
	5. Build little query engines
## Online
	1. Decide on server
	2. Export database to server
	3. Build secure website to query database on server from anywhere
	4. have RSI on Steroids!
	5. Harvest creativity from others by checking their queries


# Access BGH-Database and download every decision §treasurehunt
	1. Download decision and automatically name it right
		* Print status of download (skip to next page after loop, downloading 5 out of 76)
		* Download compare AZ to previous download from RSI
	2. Convert PDF to text
	3. Convert to meaningful JSON
		*Orientation: Tags from XML files from RSI

