nested = [[1,2],[3.4],[5]]

def flatten(nested):
  try:
    for sublist in nested:
      for element in sublist:
       yield element
  except TypeError:
    yield nested
  

for num in flatten(nested):
  print(num)