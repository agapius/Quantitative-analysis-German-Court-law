### Access BGH-Database and download every decision
1. Get Years (for loop)
2. Get pages (for loop)
3. Get EAz (for loop)
	 * Get date, Aktenzeichen and downloadlink
	 * Get Court from the other loop/ (!get court from Aktenzeichen!)
	 * download

3. Download decision and automatically name it right
4. Create decent folder structure for court and date

### Convert PDF to XML/TXT/JSON
1. TXT: Plain, simple but no tagging whatsoever. Thus no quick querying over parts of the documents
	* E.g. find all Urteile that cite Faust
2. XML: Super loaded, complicated a little overkill
3. JSon: Straight forward, super easily queried with Python
	* gives out pretty lean dictionary format
	* Recommended by some people I know

### Analyze the document and tag it (basically make a meaningful JSon File)
1. Name Tag
2. Judges tag
3. previous decisions tag
3. Citations
	* Subcategory person who is cited
	* medium that is cited
	* gives us the e.g. possibility to query all JSon BGH and give us a dictionary with the people cited and the numer of citations

### Store the documents in the JSon Format in a datbase (Computer/Database: MongoDB,...)
1. MongoDB seems like a pretty good option.
2. MongoDB has been recommended to me
3. Other options could be considered

### Build powerful analytics engine
1. Think about storage options for all decisions considering query speeds
2. Query decisions by keywords, connections, judges
3. Query using sentiment analysis and other kinds of more creative analysis

### Go online
1. Harvest creativity from others by checking their queries
2. Implement more ways to query if demanded/possible
3. Expand Scope

