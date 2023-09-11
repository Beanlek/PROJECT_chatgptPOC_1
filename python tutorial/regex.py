import re

txt = "file_bean.csv"

#Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):

x = re.search("\w.csv$", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")