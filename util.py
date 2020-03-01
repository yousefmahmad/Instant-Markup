"""
A simple way to find blocks of text in a normal text file.
Find and collect all the lines encountered within the file until you encounter and empty line. That's one block
"""

def lines(file):
  # iterating over the lines in the file
  for line in file: yield line
  # return the break
  yield '\n'
  
def blocks(file):
  block = []
  for line in lines(file):
    if line.strip():
      block.append(line)
    elif block:
      yield ''.join(block).strip()
      block = []