import re
word="Suroora"
if re.match(word,"Suroora is a programmer , Suroora is a smart girl, suroora is a woman "):
    print("word matched")
else:
    print("not matched")
print(re.findall(word,"Suroora is a programmer , Suroora is a smart girl, Suroora is a woman "))

