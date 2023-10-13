import nltk
from nltk import FreqDist
nltk.download('punkt')
nltk.download('porter_test')
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter
from nltk.stem import PorterStemmer

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

print("The 10 most common words and their count for Group A are:", fdistA.most_common(10))
print("The 10 most common words and their count for Group B are:", fdistB.most_common(10))
print("The 10 most common words and their count for Group C are:", fdistC.most_common(10))

#Question 4
total_count_all = 0  # count for total

subcorpora = [subcorpus_A, subcorpus_B, subcorpus_C]
subcorpus_names = ['Subcorpus A', 'Subcorpus B', 'Subcorpus C']

for subcorpus, name in zip(subcorpora, subcorpus_names):
    words = []
    with open(subcorpus, 'r', encoding='utf-8') as file:
        text = file.read()
        words = nltk.word_tokenize(text)


    exactly_10_characters_words = [word for word in words if len(word) == 10]


    word_counts = Counter(exactly_10_characters_words)


    subcorpus_total_count = sum(word_counts.values())
    total_count_all += subcorpus_total_count


    print(name)
    for word, count in word_counts.most_common():
        print(f'{word}: {count}')
    print(f'Total Words with 10 Characters in {name}: {subcorpus_total_count}')
    print()

print(f'Total Words with 10 Characters Across All Subcorpora: {total_count_all}')


# question 5 
subcorpora = [subcorpus_A, subcorpus_B, subcorpus_C]
subcorpus_names = ['Subcorpus A', 'Subcorpus B', 'Subcorpus C']

for subcorpus, name in zip(subcorpora, subcorpus_names):
    with open(subcorpus, 'r', encoding='utf-8') as file:
        text = file.read()

    sentences = sent_tokenize(text)

    max_length = 0
    longest_sentence = ''
    num_words = 0  # Initialize the word count

    for sentence in sentences:
        words = word_tokenize(sentence)
        num_tokens = len(words)  # Count tokens (including punctuation)
        num_words_in_sentence = len([word for word in words if word.isalnum()])  # Count only words, not punctuation

        if num_tokens > max_length:
            max_length = num_tokens
            longest_sentence = sentence
            num_words = num_words_in_sentence

    print(f"The longest sentence for {name} is:")
    print(longest_sentence)
    print(f"Number of tokens is: {max_length}")
    print(f"Number of words is: {num_words}")
    print()




 #q6 -
subcorpora = [subcorpus_A, subcorpus_B, subcorpus_C]
subcorpus_names = ['Subcorpus A', 'Subcorpus B', 'Subcorpus C']

stemmer = PorterStemmer()

for subcorpus, name in zip(subcorpora, subcorpus_names):
    words = []
    with open(subcorpus, 'r', encoding='utf-8') as file:
        text = file.read()
        words = nltk.word_tokenize(text)

    long_words = [word for word in words if len(word) >= 10]

    word_counts = Counter(long_words)

    print(name)
    for word, count in word_counts.most_common():
        print(f'{word}: {count}')
    print()

    sentences = sent_tokenize(text)

    max_length = 0
    longest_sentence = ''

    for sentence in sentences:
        words = word_tokenize(sentence)
        num_words = len(words)

        if num_words > max_length:
            max_length = num_words
            longest_sentence = sentence

    stemmed_sentence = ' '.join([stemmer.stem(word) for word in word_tokenize(longest_sentence)])

    print("Longest Sentence (Number of Words):")
    print(longest_sentence)
    print(f"Number of Words: {max_length}")
    print("Stemmed Longest Sentence:")
    print(stemmed_sentence)
    print()
