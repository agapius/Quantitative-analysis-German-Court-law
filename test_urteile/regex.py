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
            split = split.split('und')
            split = split.split('bestätigt')
            split = split.split('Hinweis')
            list_of_citations = list_of_citations + split
        else:
            list_of_citations.append(string)
    list_of_citations = clean_list(list_of_citations)
    return list_of_citations

# returns source, loops trough dictionary, values are RegExs 
def find_source(string):
    
    dictionary = {
    'BGH':              '((I |II |III |IV |V |VI |VII |VIII |IX |X |XI |XII |XIV )(ZR|ZA|ZB|ZR(Ü)|BLw|LwZR|LwZA|LwZB|GSZ|AR(VZ)|ARZ|StR|StB|GSSt|AR(VS)|AR(Vollz)|ARs|ARP|BJs|StE|BGs|AK|BGns|B|(VGS|VRG)|AR|AnwZ|AnwZ(P)|AnwZ(B)|AnwZ(Brfg)|AnwSt|AnwSt(R|B)|KZR|KZA|KZB|KVR|KVZ|KRB|AR(Kart)|EnZR|EnZA|EnZB|EnVR|EnVZ|EnRB|AR(Enw)|NotZ|NotZ(Brfg)|NotSt(B)|NotSt(Brfg)|PatAnwZ|PatAnwSt(R|B)|RiZ|RiZ(R|B)|RiSt|RiSt(R|B)|AR(Ri)|StbSt(R|B)|WpSt(R|B)))|(BGH)',

    'BVerfG':           '(BVerfG)|(Bundesverfassungsgericht)',

    'LG Hamburg':       '(LG Hamburg)|(Landgericht(s)? Hamburg)', 
    'AG Hamburg':       '(AG Hamburg)',
    'Staudinger':       '(Staudinger)',
    'OLG Hamm' :        '(OLG|Olg).*(Hamm)',
    'OLG München' :     '((OLG|Olg).*(München))|(BayObLG)',
    'OLG Stuttgart' :   '(OLG|Olg).*(Stuttgart)',
    'OLG Frankfurt' :   '(OLG|Olg).*(Frankfurt)',
    'OLG Düsseldorf' :  '(OLG|Olg).*(Düsseldorf)',
    'OLG Karlsruhe' :   '(OLG|Olg).*(Karlsruhe)',
    'OLG Dresden' :     '(OLG|Olg).*(Dresden)',
    'OLG Köln' :        '(OLG|Olg).*(Köln)',
    'OLG Celle' :       '(OLG|Olg).*(Celle)',
    'OLG Berlin' :      '(OLG|Olg).*(Berlin)',
    'OLG Nürnberg' :    '(OLG|Olg).*(Nürnberg)',
    'OLG Schleswig' :   '(OLG|Olg).*(Schleswig)',
    'OLG Koblenz' :     '(OLG|Olg).*(Koblenz)',
    'OLG Brandenburg' : '(OLG|Olg).*(Brandenburg)|Brandenburgisches OLG',
    'OLG Oldenburg' :   '(OLG|Olg).*(Oldenburg)',
    'OLG Naumburg' :    '(OLG|Olg).*(Naumburg)|OLG (des Landes)?(?=.*Sachsen-Anhalt)',
    'OLG Bamberg' :     '(OLG|Olg).*(Bamberg)',
    'OLG Jena' :        '(OLG|Olg).*(Jena)',
    'OLG Hamburg' :     '(OLG|Olg).*(Hamburg)|Hanseatisches Oberlandesgericht Hamburg' ,
    'OLG Rostock' :     '(OLG|Olg).*(Rostock)',
    'OLG Zweibrücken' : '(OLG|Olg).*(Zweibrücken)',
    'OLG Braunschweig': '(OLG|Olg).*(Braunschweig)',
    'OLG Saarbrücken':  '(OLG|Olg).*(Saarbrücken)',
    'OLG Bremen' :      '(OLG|Olg).*(Bremen)',
    'KG':               '^ ?KG[, ]|KG(?=.*Berlin)|Kammergericht|(?!=Co.) KG, ',
    'OLG Saarland':     'Saarländisches OLG|OLG Saarland',

    
    'MüKo-BGB': '(MüKo BGB)|(Mü[kK]o-?BGB)|(MünchKomm.?BGB)|(MünchKomm-BGB)|(MüKomm-BGB)|MünchKomm(?=.*BGB)|MüKo(?=.*BGB)|Münchener Kommentar zum BGB',
    'MüKo-ZPO': '(MüKo[ -/]?ZPO)|(MünchKomm.?ZPO)|(MünchKomm-ZPO)|(MünchKomm[ -/.]?ZPO)|MünchKomm(?=.*ZPO)',
    'MüKo-GmbHG': '(MünchKommGmbHG)|(MüKo-?GmbHG)|(MünchKomm-GmbHG)',
    'MüKo-InsO' : '(MüKo[ -]?InsO)|(MünchKomm[ -]?InsO)',
    'MüKo-StGB': 'Mü[kK]o[ -/]?StGB|MünchKomm[ -]?StGB|MüKomm-StGB',
    'MüKo-StPO': 'MüKo[ -]?StPO|MünchKomm[ -]?StPO',
    'MüKo-HGB'  : '(MüKo[ -.]?HGB)|(MünchKomm[ -.]?HGB)',
    'MüKo-AktG' : '(Mü[kK]o[ -.]?AktG)|(MünchKomm[ -.]?AktG)',
    
   
    'Sodan/Ziekow'      : '(Sodan+/Ziekow)', 
    
    'Staudinger': '(Staudinger)',
    'Palandt'       : '(Palandt)',
    'jurisPK-BGB': 'jurisPK[ -/]?BGB|juris Praxiskommentar BGB',

    'BeckOK-BGB'        : '(Beck[ -]?OK[ -]?BGB)',
    'BeckOK-ZPO'        : '(Beck[ -]?OK[ -]?ZPO)|Vorwerk(?=.*ZPO)|Beck\'scher Online-Kommentar ZPO',
    'BeckOK-StGB' : '(Beck[ -]?OK[ -]?StGB)',
    'BeckOK-Datenschutzrecht': '(Beck[ -]?OK[ -]?Datenschutzrecht)',
    'BeckOK-StPO'       : '(Beck[ -]?OK[ -]?StPO)',
    'BeckOK-BauGB'      : '(Beck[ -]?OK[ -]?BauGB)',
    'BeckOK-FamFG'      : '(Beck[ -]?OK[ -]?FamFG)',
    'BeckOK-HGB'        : '(Beck[ -]?OK[ -]?HGB)',
    'BeckOK-WEG'        : '(Beck[ -]?OK[ -]?WEG)',
    'BeckOK-UrhR'       : '(Beck[ -]?OK[ -]?UrhR)',
    'BeckOK-AuslR'      : '(Beck[ -]?OK[ -]?AuslR)',
    'BeckOK-GG'     : '(Beck[ -]?OK[ -]?GG)',
    'BeckOK-VVG'        : '(Beck[ -]?OK[ -]?VVG)',
    'BeckOK-GBO'        : '(Beck[ -]?OK[ -]?GBO)',
    'BeckOK-VwVfG'      : '(Beck[ -]?OK[ -]?VwVfG)',

    
    'Meyer-Goßner': '^(?!.*Festschrift.*Meyer-Goßner).*(Meyer-Goßner)',
    'Fischer': 'Fischer[ -/,]?[ ]?StGB|(Fischer, aaO)',
    'Leipziger Kommentar': 'Leipziger Kommentar',
    'Schönke/Schröder'  : '(Schönke/Schröder)', 

    'Thomas/Putzo': 'Thomas/Putzo',
    'Musielak-ZPO': 'Musielak(?=.*(ZPO)|.*(aaO))',
    'Zöller-ZPO': 'Zöller(?=.*ZPO)|Zöller/Heßler|Zöller/Vollkommer|Zöller/Stöber|Zöller/Greger|Zöller/Geimer|Zöller/Philippi',
    'Baumbach-ZPO': 'Baumbach(?=.*ZPO)|Baumbach/(Lauterbach/)?(Albers/)?Hartmann',
    'Wieczorek-ZPO': 'Wieczorek(?=/Schütze|.*ZPO)',
    'Prütting-ZPO': 'Prütting(?=/Gehrlein|.*ZPO)',
    'Hk-ZPO': 'H[kK][ -]?ZPO',
    'Stein/Jonas-ZPO': 'Stein(?=/Jonas|.*ZPO)',
    'Saenger-ZPO': 'Saenger(?=.*ZPO)|Saenger/Saenger',
    'Zimmermann-ZPO': 'Zimmermann(?=.*ZPO)',
    
    'Musielak-FamG': 'Musielak(?=.*FamFG)',
    'Baumbach-GmbH': 'Baumbach(?=.*GmbH|/Hueck)',
    'Baumbach-HGB': 'Baumbach(?=.*HGB|/Hopt)',
    'Hk-InsO': 'H[kK][ -]?InsO',
}
    
    for key, value in dictionary.items():
        if(re.search(value, string)):
            return key
    return False

def listcount(list, string):
    count = 0
    while(string in list):
        count += 1
        list.remove(string)
    return count

# prints out the percentage of the done xmls
def print_percentage(finished, total):
	percentage = (finished / total) * 100
	print(str(percentage) + '% done!')



        






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


