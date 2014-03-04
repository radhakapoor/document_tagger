import os
import sys
import re

directory = sys.argv[1] #/Users/radhakapoor/Desktop/Thinkful/document_tagger/part2/texts 

title_search = re.compile(r'(?:Title:\s*)(?P<title>(.*)[]*?\n[]*(.*))', re.IGNORECASE|re.VERBOSE)
author_search = re.compile(r'(author:)(?P<author>.*)', re.IGNORECASE)
translator_search = re.compile(r'(translator:)(?P<translator>.*)', re.IGNORECASE)
illustrator_search = re.compile(r'(illustrator:)(?P<illustrator>.*)', re.IGNORECASE)


for fl in (os.listdir(directory)):
    if fl.endswith('.txt'):       #if it's a text file
        #print 'Processing {0}.'.format(fl)

        fl_path = os.path.join(directory, fl) #the full path to the file is the directory plus
                                              #the file name

        with open(fl_path, 'r') as f:         #open the file as f
            full_text = f.read()              #assign its contents to the var full_text
            
        searches = {}    
    
        for kw in sys.argv[2:]:
            searches[kw] = re.compile(r'\b' + kw + r'\b', re.IGNORECASE)
    
    
    title = re.search(title_search, full_text).group('title')
    author = re.search(author_search, full_text)
    translator = re.search(translator_search, full_text)
    illustrator = re.search(illustrator_search, full_text)
    if author: 
        author = author.group('author')
    if translator:
        translator = translator.group('translator')
    if illustrator:
        illustrator = illustrator.group('illustrator')
    print "***" * 25
    print "Here's the info for doc {}:".format(fl)
    print "Title:  {}".format(title)
    print "Author(s): {}".format(author)
    print "Translator(s): {}".format(translator)
    print "Illustrator(s): {}".format(illustrator)
    print "\n" 
        
    print "Here's the keyword info for doc {}:".format(fl)
    for search in searches:
        print "\"{0}\": {1}".format(search, len(re.findall(searches[search], full_text)))
        