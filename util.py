"""
A simple way to find blocks of text in a normal text file.
Find and collect all the lines encountered within the file until you encounter and empty line. That's one block
"""

def lines(file):
  # basically saying to return the lines that have text
  for line in file: yield line
  # return the break
  yield '\n'