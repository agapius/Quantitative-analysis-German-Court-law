### Access Rechtsprechung-im-Internet
## Get all 14k XML Files BGH - DONE
## Get rest of XML Files -DONE
## XML
	* Unzip all (Ignore Pictures) -> full of xml
	unzip backslash*.zip -d targetdirectory (how to extract only xml?)
	* Go through *.xml and get list of all BGH-AZ und datum (count & compare to BGH since 2000)
	* Find out what "<dl><dt><dd>" stand for. 
## XML to JSon
	* Additional Tagging (most difficult)
		* Zitate mit Regex 
		* Entscheidungsträger (immer letzter/vorletzter Absatz?)
	* Conversion
		* Standart-Converter from the internet?
		* Build custom?
			*for xml-class in XML create JSon Class
			*maybe to Excel custom and then from Excel to JSon easy thus standart is ok
## JSon -> Mongo 
	*should be super easy:
	* "mongoimport --db Urteile --collection BGH/BVerwG,... --drop --file ~/documents/backslash*.json"
## Query
	*"Most cited author/Kommentar?"; "# of decisions(/decisions per judge"; "most §'s subject to debate"
	*Build little query engines
## Online
	*Decide on server
	*Export database to server
	*Build secure website to query database on server from anywhere
	*have RSI on Steroids!


### Access BGH-Database and download every decision §treasurehunt
1. Get Years (for loop)  
2. Get pages (for loop)  
3. Get EAz (for loop) 
	 * Get date, Aktenzeichen and downloadlink § treasurehunt
	 * Get Court from the other loop/ (!get court from Aktenzeichen!) 
	 * download 
4. Get vorinstanzliches Urteil 
	* später aus der Datenbank

3. Download decision and automatically name it right
	* Print status of download (skip to next page after loop, downloading 5 out of 76)
	* Downloaden - wie viel Speicherplatz?
4. Create decent folder structure for court and date

### Analyze the document and tag it (basically make a meaningful JSon File)
1. Name Tag
2. Judges tag
3. previous decisions tag
3. Citations
	* Subcategory person who is cited
	* medium that is cited
	* gives us the e.g. possibility to query all JSon BGH and give us a dictionary with the people cited and the numer of citations


### Build powerful analytics engine
1. Think about storage options for all decisions considering query speeds
2. Query decisions by keywords, connections, judges
3. Query using sentiment analysis and other kinds of more creative analysis
4. "Andere kauften auch"-Option (was haben sich andere angeschaut, die dieses Urteil angesehen haben)

### Go online
1. Harvest creativity from others by checking their queries
2. Implement more ways to query if demanded/possible
3. Expand Scope
4. Find Cloud Storage

