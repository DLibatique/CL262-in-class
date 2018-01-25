# CL262-in-class

This is a repo for use in CL262, 'Homeric Epic', a Classical Studies course at Boston University in the spring of 2018, taught by [Daniel Libatique](https://twitter.com/DLibatique10).

## files
This directory contains all files relating to the weekly assignments -- each filename begins with the due date of the assignment. Files for each assignment are spread out among the following subdirectories:
* **plain_text**: plain text files (OCR-ed from Benner's text and manually corrected),
* **bridge_vocab_lists**: a vocabulary list (courtesy of [The Bridge](http://bridge.haverford.edu)),
* **benner_notes**: Benner's notes on the lines in question (courtesy of Perseus), and
* **steadman**: for the selections from Books 6 and 22, the appropriate pages from Steadman's commentary, with vocab and notes on the same page as the text.

## projector.txt
This file displays the text that is to be projected onto the blackboard/whiteboard.

## projector_prep.py
This script cleans up the Benner snippets in files/plain_text. You can use the following code to load the text for the class in question.

`
$ cd CL262-in-class
$ python
$ import projector_prep
$ projector_prep.write_to_projector('files/plain_text/<filename>)
`

*Voilà*! You have the assignment ready to project in **projector.txt**.