### Access Rectsprechung-im-Internet
1. Get all 14k XML Files BGH
2. Get rest of XML Files
3. Compare to BGH Files (by AZ) - if there is stuff missing, etc
4. Understand Tagging conventionsTags for citations (for all stuff in brackets in tags, if NJW, BGHZ,... in Brackets otherwise add to list)
5. Convert to JSON or directly pipe it into MongoDB


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

### Decide XML/TXT/JSON
1. TXT: Plain, simple but no tagging whatsoever. Thus no quick querying over parts of the documents
	* E.g. find all Urteile that cite Faust
2. XML: Super loaded, complicated a little overkill
3. JSon: Straight forward, super easily queried with Python
	* gives out pretty lean dictionary format
	* Recommended by some people I know
	
### MongoResearch
1. Was brauchen wir für ein Format um einzuspeisen?
2. Wie speisen wir ein?
3. Was für Queries sind möglich?

### Convert PDF to JSON
1. Convert PDF to plain Text (less keeps formatting) and then to JSON and then tag the parts
	* What sections need to be tagged?
	* Vorinstanz, beteiligte Richter, wenn vorhanden auch einzelne Zitate
	* Wie taggen? regex using the formatting? Using key phrases
2. Find a solution to diectly convert to JSON and get it tagged automtically?

### Analyze the document and tag it (basically make a meaningful JSon File)
1. Name Tag
2. Judges tag
3. previous decisions tag
3. Citations
	* Subcategory person who is cited
	* medium that is cited
	* gives us the e.g. possibility to query all JSon BGH and give us a dictionary with the people cited and the numer of citations

### Store the documents in the JSon Format in a database (Computer/Database: MongoDB,...)
1. MongoDB seems like a pretty good option.
2. MongoDB has been recommended to me
3. MongoDB entschieden

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

