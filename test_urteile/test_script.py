import re
import sys

## first command line argument is the regex, the script will write all hits in
## a file with the name of the script and everythin else in citations_reduced. 
## After first use the open will should also be citations_reduced

output_counter = 0
regular_expression = sys.argv[1]

filename = regular_expression.replace('.', '').replace('/', '') + '.txt'
#filename = 'bgh2.txt'
ergebnisse = open(filename, 'w')

with open('citations_reduced.txt', 'r') as input:
	lines = input.readlines()
	input_counter = (len(lines))
	input.close()

with open('citations_reduced.txt', 'w+') as output:
	for line in lines:
		if(re.search(regular_expression, line)):
			ergebnisse.write(line)
		else:
			output.write(line)
			output_counter= output_counter +1

print('\n')
print(regular_expression)
print('captured %d citations.' %(input_counter - output_counter))
