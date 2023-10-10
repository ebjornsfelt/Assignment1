import nltk

fantasyfile = "FICTION-fantasy.txt"
scififile = "FICTION-sci-fi.txt"
thrillerfile = "FICTION-thriller.txt"

with open(fantasyfile, 'r', encoding='utf-8') as file:
    groupA = file.read()

with open(scififile, 'r', encoding='utf-8') as file:
    groupB = file.read()
    
with open(thrillerfile, 'r', encoding='utf-8') as file:
    groupC = file.read()
    
lengthA = len(groupA)
lengthB = len(groupB)
lengthC = len(groupC)

# Question 1: Length of subgenre 
print(lengthA)
print(lengthB)
print(lengthC)