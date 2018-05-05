# STORYBOT - a language processing project

This chatbot is a proof-of-concept for a story-telling AI. 

A story is generated with several characters, locations and objects. The characters interact with one another, can pick up objects and move from a location to another one. The user will be able to ask the chatbot questions about the story and even make suggestions to the chatbot in order to influence the story.

## Motivation

This is a fourth-year computer engineering project which aims to teach us about Python and natural-language processing. It is a widely studied computer science field, allowing many real-world applications such as personal assistants and real-time translation.

Natural-language processing has many challenges we encountered. Because of the small scale of this project, we didn't attempt to solve them: for example, syntaxic and semantic ambiguity is one of the most apparent flaw of the chatbot. We believe nonetheless that NLP is a major field we will take time to discover.

## Implemented features

The chatbot is able to answer using three modes. Mode 3 is the main story mode. It uses a system of tags: the user's input sentece is associated with a list of tags generated from a database of about 60 tags. This list is used to find a suitable answer in another database which contains several answers, each one corresponding to a tag list.

Mode 2 is a simplified Mode 3 : in case Mode 3 is not able to compute an answer, Mode 2 will give a simpler answer by re-associating the same sentence with only one tag. 

Mode 1 does not use tag recognition and whatever the user says, the chatbot will answer with 'backchannels', such as `Uhh..` or `Hmm…`.

Further explanations can be found in French (`/misc/Rapport.pdf`).

## Tech used

The NLTK library was used, especially its tokenize function: it is able to separate contractions and negations. Our chatbot is thus able to recognize I'm and I am as the same expression, for example.

## How to run?

To run the program, several modules are to be used: NLTK, NumPy and Re. For NLTK, downloading an extra package may be required: 

`pip install nltk`
`python -m nltk.downloader 'punkt'`

The `punkt` package is included as well with this git (`/nltk_data/tokenizers`). In case the NLTK downloader is broken, you can copy the whole folder into:
- Windows: `C:\nltk_data\tokenizers`
- Mac OS: `/usr/local/share/nltk_data/tokenizers`
- Unix: `/usr/share/nltk_data/tokenizers`

The command used to run the project is:

`python main.py`

## Use examples

When running the chatbot, the user can ask questions such as:
- Where is Annie?
- What is she doing?

To which the chatbot will be able to answer:
- Annie is in the kitchen.
- Annie is preparing food.

## Troubleshooting

Make sure your Python 3 install is up to date as some functions have been renamed (`iteritems()` and `.raw_input()` for example)

## Future development

Possible areas for improvment would be:

- adding verbs and noun tagging, 
- adding partial answers the chatbot will combine,
- fixing typos such as blank spaces before question marks,
- implementing a 'context' system for the chatbot to remember about the conversation's subject for example,
- and of course adding more tags.


## Bonus: the simulation's parameters

5 CHARACTERS

Annie, Antoine, Maria, Jeffery, Laura.

Each character is defined by :
-its name and last name
-its gender
-In which room he is in
-the objects he carries
-his state of mind at the moment
-his physical health
-his nutrition, hydration and sleep levels
-his relationship with the other characters


THE ROOM(s) :

Living room, kitchen, toilets, bathroom, roof, a bedroom for each character, and the outside.

Each room is defined by :
-its name
-its state (messy, wrecked, tidy…)
-if people can acces it
-who is inside
-what it contains (tools, ressources, and entertainments)

THE RESSOURCES :

They are consumed when used, and have different effect depending on what they are.
The different ressources that appear in the simulation are :
-Water
-Basic Food
-Well Prepared food
-Medicines
-Alcohol

THE ENTERTAINMENTS :

The different entertainments that appear in the simulation are :
-TV
-Deck of cards
-Books
-Computer

THE TOOLS :

The different tools available in the simulation are :
-Crowbar
-Gun
-Rifle
-Torchlamp
-might add more later


## Project members

Adrien Lavillonnière (`Veados`)

Corentin Manscour (`neofoetus`)

Hien Minh Nguyen (`shipanda01`)

Polytech-Paris Sud