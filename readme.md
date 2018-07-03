# Access Rechtsprechung-im-Internet
## Update the Zip-Files automatically
## Unzip the files
	1. Unziper.py unzips all zip files that are KORE*.zip
	2. Unzip other files and ignore pictures etc
	JURE 	KORE(zivilsenat) BGH(Strafsenat)E 
	STRE 	BFH
	WBRE 	BVERWGE
	MPRE 	BPatG
	 	BVerfG
## Tagging
	1. Load citations_reduced.txt into sublime
	2. Create Regex for remaining source
		*create a remainder file that collects all the citations that have not yet been tagged
		*create a strng compare function for the citations in the "not-yet-tagges"-file and compare all
		*function to group somewhat similar strings and write a regex accordingly
		*let the community review and approve suggested regexes (might be overengeneered but AI, yey!)
	3. Run test_script.py with this Regex
		* Outputs a list of all results captured by Regex
		* Reduces citations_reduced.txt by everything the new Regex captures
	4. Check results
	5. Copy working Regex into sources.txt

## XML to JSon
	1. Additional Tagging 
		* Use Regexes and create additional tags
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

# Access BGH-Database and download every decision
	1. Download decision and automatically name it right (treasurehunt3)
		* Print status of download (skip to next page after loop, downloading 5 out of 76)
		* Download compare AZ to previous download from RSI
	2. Convert PDF to text
	3. Convert to meaningful JSON
		*Orientation: Tags from XML files from RSI

