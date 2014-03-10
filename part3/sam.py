# Preconditions
# full_text of the gutenberg article
# list of keyword strings 

#Post conditions
# print summary
def print_keyword_summary():
  pass



# Preconditions
# pass in the full text of the gutenberg article
# Postconditions
# Print to the screen title author, translator...etc other metadata
def print_file_metadata(full_text):
  pass


# Preconditions
# argv contains a path to gutenberg files and a list of keywords
# Postcondtions
# print to the screen the metadata and keyword search for all files in path.
def main():
    path = sys.argv[1]

  # list files in path
  # iterate  (or enumerate) over files
  # send full text to print_keyword and print_file_metadata

  # os.listdir(path)
  # fullpath = os.path.join(path, filename)
  # open...
  # read


  print_file_metadata(full_text)
  print_keyword_summary(full_text)
