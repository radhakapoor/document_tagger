import re

DIV_COMM = """
Project Gutenberg's The Divine Comedy, Complete, by Dante Alighieri
 
This eBook is for the use of anyone anywhere at no cost and with
almost no restrictions whatsoever.  You may copy it, give it away or
re-use it under the terms of the Project Gutenberg License included
with this eBook or online at www.gutenberg.org
 
 
Title: The Divine Comedy, Complete
       The Vision of Paradise, Purgatory and Hell
 
Author: Dante Alighieri
 
Illustrator: Gustave Dore
 
Translator: Rev. H. F. Cary
 
Release Date: September, 2005  [Etext #8800]
Posting Date: June 11, 2009
 
Language: English
 
 
*** START OF THIS PROJECT GUTENBERG EBOOK THE DIVINE COMEDY, COMPLETE ***
[...]
His glory, by whose might all things are mov'd,
Pierces the universe, and in one part
[...]
End of Project Gutenberg's The Divine Comedy, Complete, by Dante Alighieri
*** END OF THIS PROJECT GUTENBERG EBOOK THE DIVINE COMEDY, COMPLETE ***
***** This file should be named 8800.txt or 8800.zip *****
This and all associated files of various formats will be found in:
        http://www.gutenberg.org/8/8/0/8800/
[...]
"""
# need to re-write this as verbose. see this re verbose http://docs.python.org/2/library/re.html
match = re.search(r'Title:(.*\n.*)', DIV_COMM, re.IGNORECASE)

#title_search = re.compile(r'Title:'), re.VERBOSE)


'''
if match:
    print match.group
else:
    print "no match"
'''