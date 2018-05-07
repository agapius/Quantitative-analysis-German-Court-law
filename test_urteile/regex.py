import re

# returns a list of mostly citations
def clean_list(list):
    clean_list = []
    for item in list:
        if(test_of_tests(item)):
            clean_list.append(item.replace('vgl. ', ''))
    
    return clean_list

# returns true if string is an article-citation
def test_for_article(string):
    return bool(re.search('^§', string))

# returns true if string has numbers (citations will have numbers), 
# currently not used, but included in test for citations
def test_for_has_numbers(string):
    return bool(re.search(r'\d', string))

# returns true is string 
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

# returns a list of mostly citations
def scan_paragraph(string):
    pattern_brackets = '\((.*?)\)'
    regex_brackets = re.compile(pattern_brackets)
    list_of_brackets = re.findall(regex_brackets, string)
    list_of_citations = []
    for string in list_of_brackets:
        if(';' in string):
            split = string.split(';')
            list_of_citations = list_of_citations + split
        else:
            list_of_citations.append(string)
    list_of_citations = clean_list(list_of_citations)
    return list_of_citations


# KORE303862016.xml
# MPRE176760964.xml
# KORE317722010.xml
'''
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
    print(string)'''


