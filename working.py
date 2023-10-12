import nltk
nltk.download('punkt')
nltk.download('porter_test')
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter
from nltk.stem import PorterStemmer

subcorpus_A = "C:\\Users\\ken\\Desktop\\Assignment1-main\\FICTION-fantasy.txt"
subcorpus_B = "C:\\Users\\ken\\Desktop\\Assignment1-main\\FICTION-sci-fi.txt"
subcorpus_C = "C:\\Users\\ken\\Desktop\\Assignment1-main\\FICTION-thriller.txt"

# ethans part
#with open(subcorpus_A, 'r', encoding='utf-8') as file:
#    groupA = file.read()

#with open(subcorpus_B, 'r', encoding='utf-8') as file:
#    groupB = file.read()

#with open(subcorpus_C, 'r', encoding='utf-8') as file:
#    groupC = file.read()

#lengthA = len(groupA)
#lengthB = len(groupB)
#lengthC = len(groupC)

# These parts are still active:
#print(lengthA)
#print(lengthB)
#print(lengthC)

# # question4-  words with EXACTLY 10 characters long and their counts
# total_count_all = 0  # count for total

# subcorpora = [subcorpus_A, subcorpus_B, subcorpus_C]
# subcorpus_names = ['Subcorpus A', 'Subcorpus B', 'Subcorpus C']

# for subcorpus, name in zip(subcorpora, subcorpus_names):
#     words = []
#     with open(subcorpus, 'r', encoding='utf-8') as file:
#         text = file.read()
#         words = nltk.word_tokenize(text)

#     #  words exactly 10 
#     exactly_10_characters_words = [word for word in words if len(word) == 10]

#     # occurrences of  exactly 10-character word
#     word_counts = Counter(exactly_10_characters_words)

#     # calculate total count for this subcorpus and add it to the total 
#     subcorpus_total_count = sum(word_counts.values())
#     total_count_all += subcorpus_total_count

#     ####results
#     print(name)
#     for word, count in word_counts.most_common():
#         print(f'{word}: {count}')
#     print(f'Total Words with 10 Characters in {name}: {subcorpus_total_count}')
#     print()

# # deesplaydisplayDISPLAYREMEMBERTODISPLAY
# print(f'Total Words with 10 Characters Across All Subcorpora: {total_count_all}')



# # question 5 - longest sentence hint use nltk 2.1
# subcorpora = [subcorpus_A, subcorpus_B, subcorpus_C]
# subcorpus_names = ['Subcorpus A', 'Subcorpus B', 'Subcorpus C']

# for subcorpus, name in zip(subcorpora, subcorpus_names):
#     with open(subcorpus, 'r', encoding='utf-8') as file:
#         text = file.read()

#     # tokenize text into sentences using ->>sent_tokenize<<-- too much swag command
#     sentences = sent_tokenize(text)

#     # find longest sentence and count tokens and words 
#     max_length = 0
#     longest_sentence = ''
#     num_words = 0  # Initialize the word count

#     for sentence in sentences:
#         words = word_tokenize(sentence)
#         num_tokens = len(words)  # Count tokens (including punctuation)
#         num_words_in_sentence = len([word for word in words if word.isalnum()])  # Count only words, not punctuation

#         if num_tokens > max_length:
#             max_length = num_tokens
#             longest_sentence = sentence
#             num_words = num_words_in_sentence

#     # printntntnt print rptint rpint
#     print(f"The longest sentence for {name} is:")
#     print(longest_sentence)
#     print(f"Number of tokens is: {max_length}")
#     print(f"Number of words is: {num_words}")
#     print()

# # #q6 - stemmed version of longest sentence
# subcorpora = [subcorpus_A, subcorpus_B, subcorpus_C]
# subcorpus_names = ['Subcorpus A', 'Subcorpus B', 'Subcorpus C']

# ###porterstremmercomand 
# stemmer = PorterStemmer()

# for subcorpus, name in zip(subcorpora, subcorpus_names):
#     words = []
#     with open(subcorpus, 'r', encoding='utf-8') as file:
#         text = file.read()
#         words = nltk.word_tokenize(text)

#     # filter words at least 10
#     long_words = [word for word in words if len(word) >= 10]

#     # count occurance of long word
#     word_counts = Counter(long_words)

#     # print result
#     print(name)
#     for word, count in word_counts.most_common():
#         print(f'{word}: {count}')
#     print()

#     # tokenize
#     sentences = sent_tokenize(text)

#     # finding long sentence count how many
#     max_length = 0
#     longest_sentence = ''

#     for sentence in sentences:
#         words = word_tokenize(sentence)
#         num_words = len(words)

#         if num_words > max_length:
#             max_length = num_words
#             longest_sentence = sentence

#     # stem long sentence
#     stemmed_sentence = ' '.join([stemmer.stem(word) for word in word_tokenize(longest_sentence)])

#     # print long sentence + number words
#     print("Longest Sentence (Number of Words):")
#     print(longest_sentence)
#     print(f"Number of Words: {max_length}")
#     print("Stemmed Longest Sentence:")
#     print(stemmed_sentence)
#     print()