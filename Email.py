import re
mail=input()
if re.match("^[a-z0-9._]*@[a-z]*[\.][a-z]*[\.a-z]?$",mail):
    print("Valid")
else:
    print("Not Valid")