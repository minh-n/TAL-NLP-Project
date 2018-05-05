#
#
#

import nltk 
from nltk.tokenize import word_tokenize

#to run the program using NLTK, downloading an extra package may be needed:
#(python/py3) -m nltk.downloader 'punkt'

#tokenize a given sentence, using nltk's word_tokenize 
def tokenizeSentence(sent):

    sentWordList = word_tokenize(sent)

    return sentWordList

#Legacy tokenise function. Currently unused
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
