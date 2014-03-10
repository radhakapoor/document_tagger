import sys
import re
import os

# Preconditions
# full_text of the gutenberg article
# list of keyword strings 

#Post conditions
# print summary
def print_keyword_summary(full_text, keywords):
    #for i, full_text in enumerate(full_text):
        searches = {}
        for keyword in keywords:
            searches[keyword] = re.compile(r'\b' + keyword + r'\b', re.IGNORECASE)            
        for search in searches:
            print "\"{0}\": {1}".format(search, len(re.findall(searches[search], full_text)))

# Preconditions
# pass in the full text of the gutenberg article

# Postconditions
# Print to the screen title author, translator...etc other metadata
def print_file_metadata(full_text, fl):  
  title_search = re.compile(r'(?:Title:\s*)(?P<title>(.*)[]*?\n[]*(.*))', re.IGNORECASE|re.VERBOSE)
  author_search = re.compile(r'(author:)(?P<author>.*)', re.IGNORECASE)
  translator_search = re.compile(r'(translator:)(?P<translator>.*)', re.IGNORECASE)
  illustrator_search = re.compile(r'(illustrator:)(?P<illustrator>.*)', re.IGNORECASE)
  
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
  print "\n" 
  print "Here's the keyword report:"
  
# Preconditions
# argv contains a path to gutenberg files and a list of keywords
# Postcondtions
# print to the screen the metadata and keyword search for all files in path.
def main():
    path = sys.argv[1]
    keywords = sys.argv[2:]    
    for fl in (os.listdir(path)):  #for each item that appears in the directory
        if fl.endswith('.txt'):       #if it's a text file
            

            fl_path = os.path.join(path, fl) #the full path to the file is the directory plus
                                              #the file name
            #print fl
            with open(fl_path, 'r') as f:         #open the file as f
                full_text = f.read()              #assign its contents to the var full_text
                print_file_metadata(full_text, fl)                
                print_keyword_summary(full_text, keywords)    
    

  # list files in path
  # iterate  (or enumerate) over files
  # send full text to print_keyword and print_file_metadata [how "send" full text to print_keyword and print_file_metadata?]

  # os.listdir(path)
  # fullpath = os.path.join(path, filename)
  # open...
  # read   

if __name__ == '__main__':
    main()
    
