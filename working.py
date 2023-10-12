import nltk
from nltk import FreqDist

#File opening and reading code.
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
# Print the length of each subgenre
print("Length of Group A:", lengthA)
print("Length of Group B:", lengthB)
print("Length of Group C:", lengthC)

#Question 2: Lexical diversity
# Tokenize the text excluding the repeating words.
wordsA = sorted(set(w.lower() for w in groupA if w.isalpha()))
wordsB = sorted(set(w.lower() for w in groupB if w.isalpha()))
wordsC = sorted(set(w.lower() for w in groupC if w.isalpha()))

lexical_diversity_A = len(wordsA) / len(groupA.split())
lexical_diversity_B = len(wordsB) / len(groupB.split())
lexical_diversity_C = len(wordsC) / len(groupC.split())

print("Lexical diversity Group A:", lexical_diversity_A)
print("Lexical diversity Group B:", lexical_diversity_B)
print("Lexical diversity Group C:", lexical_diversity_C)

#Question 3: 10 most frequent words
# Tokenize without excluding the repeating words.
wordsAnonunique = groupA.lower().split()
wordsBnonunique = groupB.lower().split()
wordsCnonunique = groupC.lower().split()

fdistA = FreqDist(wordsAnonunique)
fdistB = FreqDist(wordsBnonunique)
fdistC = FreqDist(wordsCnonunique)

print("The 10 most common words and their count are:", fdistA.most_common(10))
print("The 10 most common words and their count are:", fdistB.most_common(10))
print("The 10 most common words and their count are:", fdistC.most_common(10))

#Question 4
