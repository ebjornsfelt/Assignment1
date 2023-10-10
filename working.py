import nltk

grrr = "D:\SFU WORK\Fall 2023\SDA 250\Assignment1\Assignment1\FICTION-fantasy.txt"
# A = "./Assignment1/FICTION-fantasy.txt"
# B = "./Assignment1/FICTION-sci-fi.txt"
# C = "./Assignment1/FICTION-thriller.txt"

with open(grrr, 'r', encoding='utf-8') as file:
    groupA = file.read()

# with open(B, 'r', encoding='utf-8') as file:
    groupB = file.read()
    
# with open(C, 'r', encoding='utf-8') as file:
    groupC = file.read()
    
lengthA = len(groupA)
lengthB = len(groupB)
lengthC = len(groupC)


print(lengthA)