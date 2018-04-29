#
#
#

import nltk 
from nltk.tokenize import word_tokenize


#to run the program using NLTK, downloading an extra package may be needed:
#(python/py3) -m nltk.downloader 'punkt'


def read_paragraph_file(fname):

    para = []
    	
    #ouverture automatique du fichier
    with open(fname, "r") as fp:

        for line in fp.readlines():
            if line.strip() == "": continue 	#on saute les lignes vides
            para.append(line.strip())	

    return para

def write_paragraph_file(list_paras, fname):

    with open(fname, "w") as fp:

        for line in list_paras:
            fp.write(line+"\n")


def read_word_list_file(fname):
    motsliste = []

    #ouverture automatique du fichier
    with open(fname, "r") as fp:

        for line in fp.readlines():
            word = line.strip() # remove whitespace
            if word=="": continue #on saute les lignes vides
            motsliste.append(word)

    return motsliste

def write_word_list_file(motsliste, fname):

    with open(fname, "w") as fp:

        for word in motsliste:
            fp.write(word+"\n")    

def read_tab_separated_file(fname):

    rows = []

    with open(fname, "r") as fp:

        for line in fp.readlines():
            line = line.strip() 
            if line=="": continue 
            rows.append(line.split("\t")) 

    return rows 

def read_tab_separated_file(fname):

    rows = []
    with open(fname, "r") as fp:

        for line in fp.readlines():
            line = line.strip() 
            if line == "": continue 
            rows.append(line.split("\t"))

    return rows 


def write_tab_separated_file(rows, fname):

    with open(fname, "w") as fp:

        for row in rows:
            fp.write("\t".join(row)) 
            fp.write("\n")



#tokenize a given sentence, using nltk's word_tokenize 
def tokenizeSentence(sent):

    sentWordList = word_tokenize(sent)

    return sentWordList


def tokenise_en(sent):

    sent = re.sub("([^ ])\'", r"\1 '", sent) # separate apostrophe from preceding word by a space if no space to left
    sent = re.sub(" \'", r" ' ", sent) # separate apostrophe from following word if a space if left

    # separate on punctuation
    cannot_precede = ["M", "Prof", "Sgt", "Lt", "Ltd", "co", "etc", "[A-Z]", "[Ii].e", "[eE].g"] # non-exhaustive list
    regex_cannot_precede = "(?:(?<!"+")(?<!".join(cannot_precede)+"))"
    sent = re.sub(regex_cannot_precede+"([\.\,\;\:\)\(\"\?\!]( |$))", r" \1", sent)
    sent = re.sub("((^| )[\.\?\!]) ([\.\?\!]( |$))", r"\1\2", sent) # then restick several fullstops ... or several ?? or !!
    sent = sent.split() # split on whitespace
    return sent






#tab = read_paragraph_file("./TD1_files/personal_pronouns.fr.tsv")
#write_paragraph_file(tab, "blablatab")

#texte = read_paragraph_file("./TD1_files/alice.en.paras")
#write_paragraph_file(texte, "blabla")

#listname = read_word_list_file("./TD1_files/welsh_places.en.list")
#write_paragraph_file(listname, "blabla2")