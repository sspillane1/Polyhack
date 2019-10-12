import nltk
import heapq
import itertools
from operator import itemgetter


def summarize(input_text):
    stops = nltk.corpus.stopwords.words('english')

    word_list = nltk.word_tokenize(input_text)

    cleaned_words = []
    for word in word_list:
        if word not in stops:
            cleaned_words.append(word)

    cleaned_sentence = ' '.join(cleaned_words)

    sentence_list = nltk.sent_tokenize(cleaned_sentence)

    word_table = {}

    for word in cleaned_words:
        if word not in word_table.keys():
            word_table[word] = 1.0
        else:
            word_table[word] += 1.0

    for word in word_table.keys():
        word_table[word] = word_table[word] / max(word_table.values())

    cleaned_sentence = nltk.sent_tokenize(cleaned_sentence)

    sentence_table = {}

    for sent in sentence_list:
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_table.keys():
                if sent not in sentence_table.keys():
                    sentence_table[sent] = word_table[word]
                else:
                    sentence_table[sent] += word_table[word]

    for sentence in range(len(sentence_list)):
        sentence_list = nltk.sent_tokenize(input_text)
        sentence_table[sentence_list[sentence]] = sentence_table.pop(cleaned_sentence[sentence])

    top = heapq.nlargest(10, sentence_table.items(), itemgetter(1, 0))

    result = []
    for key, value in top:
        result.append(key)

    return ' '.join(result)


print(summarize("Hi there Berry! What are you doing today?"))
