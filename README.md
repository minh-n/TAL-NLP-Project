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

Further explanations can be found in French (`/misc/rapport.pdf`).

## Tech used

The NLTK library was used, especially its tokenize function: it is able to separate contractions and negations. Our chatbot is thus able to recognize I'm and I am as the same expression, for example.

## How to run?

To run the program using NLTK, downloading an extra package may be required: 

`python -m nltk.downloader 'punkt'`

The package is included as well with this git (`/nltk_data/tokenizers`)

The command used to run the project is:

`python main.py`

## Troubleshooting

It may be needed to replace the *input()* function with *raw_input()* when using Mac OS. 

## Future development

Possible areas for improvment would be:

- adding verbs and noun tagging, 
- adding partial answers the chatbot will combine,
- fixing typos such as blank spaces before question marks,
- implementing a 'context' system for the chatbot to remember about the conversation's subject for example,
- and of course adding more tags.

## Project members

Adrien Lavillonnière (`Veados`)

Corentin Manscour (`neofoetus`)

Hien Minh Nguyen (`shipanda01`)