This file is a collection of known problems and shortcomings.  

#1 Two quotes in one line  

Wegmann in Bauer/v. Oefele, GBO, 3. Aufl., § 47 Rn. 108 und in BeckOK-BGB, 39. Edition, § 1094 Rn. 11 (1)

BeckOK BGB/Hahn [Stand: 1. August 2016] § 1600 b Rn. 5 und wohl auch Staudinger/Rauscher [2011] § 1600 b Rn. 38 (1)

 Rahn, BWNotZ 1956, 89, 92 gibt lediglich die Ansicht von Palandt, BGB, 15. Aufl. wieder, ohne selbst zur Anwendbarkeit eines Rechtsgedankens aus § 816 Abs. 1 Satz 2 BGB oder § 826 BGB Stellung zu nehmen (2)

  Palandt/Weidenkaff BGB 71. Aufl. Einf. vor § 535 Rn. 122, § 566 Rn. 17, Scheuer in: Bub/Treier Handbuch der Geschäfts- und Wohnraummiete 3. Aufl. Kap. V Rn. 268 (2)

##Description  
Two quotes in one line.

##Where?   
(1) (Beck-OK-BGB)|(BeckOK-BGB)|(Bec.....txt after running test_script.txt with regex (Beck-OK-BGB),(BeckOK-BGB),(Beck OK BGB),(BeckOK BGB)'

(2) test_script.txt with Regex 'Palandt'

##Diagnosis  
Problem is that scan_paragraph()-Function (regex.py) assumes that all quotes are seperated by an ';', however, some are not. A more sophisticated approach might fix this. 

##Frequency  
Seems not to occure terribly often, around twice per source/regex. 

##Fixed  
not yet

