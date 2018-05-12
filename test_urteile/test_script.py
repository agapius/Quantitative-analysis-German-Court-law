import re
import sys

## first command line argument is the regex, the script will write all hits in
## a file with the name of the script and everythin else in citations_reduced. 
## After first use the open will should also be citations_reduced

regular_expression = sys.argv[1]
ergebnisse = open(regular_expression, 'r+')

with open('citations.txt', 'r') as input:
	with open('citations_reduced.txt', 'r+') as output:
		for line in input:
			if(re.search(regular_expression, line)):
				ergebnisse.write(line)
			else:
				output.write(line)

