import re

def clean_list(list):
	clean_list = []
	for item in list:
		if(test_of_tests(item)):
			clean_list.append(item.replace('vgl. ', ''))
	
	return clean_list

def test_for_article(string):
	return bool(re.search('^§', string))

def test_for_has_numbers(string):
	return bool(re.search(r'\d', string))


def test_for_citation(string):
	if(len(string) <= 3):
		return False
	else:
		return bool(re.search(r'\d', string))

def test_of_tests(string):
	if(test_for_citation(string) and not test_for_article(string) and test_for_has_numbers(string)):
		return True
	else:
		return False




# KORE303862016.xml
# MPRE176760964.xml
# KORE317722010.xml

f = open('KORE317722010.xml', 'r')
string = f.read()


pattern_brackets = '\((.*?)\)' # regular expression

regex_brackets = re.compile(pattern_brackets)

list_of_brackets = re.findall(regex_brackets, string)

for string in list_of_brackets:
	print(string)

list_of_citations = []

for string in list_of_brackets:
	if(';' in string):
		split = string.split(';')
		list_of_citations = list_of_citations + split
	else:
		list_of_citations.append(string)


list_of_citations = clean_list(list_of_citations)

print('CLEAN')
for string in list_of_citations:
	print(string)


