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


# Question 1: Length of subgenre 
lengthA = len(groupA)
lengthB = len(groupB)
lengthC = len(groupC)

# Print the length of each subgenre
print("Length of Group A:", lengthA)
print("Length of Group B:", lengthB)
print("Length of Group C:", lengthC)

#Question 2: Lexical diversity
# Tokenize the text into words
tokensA = nltk.word_tokenize(groupA)
tokensB = nltk.word_tokenize(groupB)
tokensC = nltk.word_tokenize(groupC)

# Calculate lexical diversity (unique words / total words)
lexical_diversity_A = len(set(tokensA)) / len(tokensA)
lexical_diversity_B = len(set(tokensB)) / len(tokensB)
lexical_diversity_C = len(set(tokensC)) / len(tokensC)


