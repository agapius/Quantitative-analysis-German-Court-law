import re
import sys


'''first command line argument is the regex, the script will write all hits in
a file with the name of the script and everythin else in citations_reduced. 
After first use the open will should also be citations_reduced'''

########################### REggexes ##########################################
regexes_dict={
'Meyer-Goßner' 		: '(Meyer-Goßner)',
'MüKo-BGB'			: '(MüKo BGB)|(MüKoBGB)|(MüKo-BGB)|(MünchKommBGB)|(MünchKomm-BGB)',
'MüKo-ZPO'			: '(MüKoZPO)|(MüKo-ZPO)|(MünchKommZPO)|(MünchKomm-ZPO)|(MünchKomm ZPO)]',
'MüKo-GmbHG'		: '(MünchKommGmbHG)|(MüKo-GmbHG)|(MüKoGmbHG)|(MünchKomm-GmbHG)',
'MüKo-InsO'			: '(MüKoInsO)|(MüKo-InsO)|(MünchKommInsO)|(MünchKomm-InsO)',
'Schönke/Schröder'	: '(Schönke/Schröder)', 
'Sodan/Ziekow'		: '(Sodan+/Ziekow)',
'Staudinger'		: '(Staudinger)',
'Palandt'			: '(Palandt)',
'BeckOK-BGB'		: '(Beck-OK-BGB)|(BeckOK-BGB)|(Beck OK BGB)|(BeckOK BGB)',
'BeckOK-ZPO'		: '(BeckOK-ZPO)|(BeckOK ZPO)|(Beck OK ZPO)',
}


############################# START ###########################################

#Counter for the lines (# of citations) in citations.txt
input_line_count=0
#Counter for the lines in output file
output_line_count=0


for key, value in regexes_dict.items():
	regular_expression = value
	#List of all captured citations
	ergebnisse = []
	
	
	
	with open('citations.txt', 'r') as citations:
		with open('citations_reduced.txt', 'r+') as citations_reduced:
			for line in citations:
				input_line_count = input_line_count+1
				if(re.search(regular_expression, line)):
					ergebnisse.append(line)
				else:
					citations_reduced.write(line)
					output_line_count = output_line_count
		print('%s captured:' %(regular_expression))
		print('%d lines' %(len(ergebnisse)))
		citations=citations_reduced

##Output list of all captured citations
'''for citation in ergebnisse:
	print(citation)
print('\n')'''

##Output length of input and output
print('\n')
print('The input file was %d lines long' %(input_line_count)) 
print('The output file is only %d lines long' %(output_line_count))
print('Congratulations, you captured %d lines' %(len(ergebnisse)))
print('\n')
