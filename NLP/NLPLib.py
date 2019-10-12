import nltk

stops = nltk.corpus.stopwords.words('english')


input_sentence = "Barry was a boy who liked berries. He ate so many berries that he was buried."



word_list = nltk.word_tokenize(input_sentence)

cleaned_words=[]
for word in word_list:
    if word not in stops:
        cleaned_words.append(word)

cleaned_sentence= ' '.join(cleaned_words)


sentence_list=nltk.sent_tokenize(cleaned_sentence)

word_table = {}

for word in cleaned_words:
    if word not in word_table.keys():
        word_table[word] = 1.0
    else:
        word_table[word] += 1.0

for word in word_table.keys():
    word_table[word]=word_table[word]/max(word_table.values())

cleaned_sentence=nltk.sent_tokenize(cleaned_sentence)

sentence_table = {}

for sent in sentence_list:
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_table.keys():
            if len(sent.split(' ')) < 30:
                if sent not in sentence_table.keys():
                    sentence_table[sent] = word_table[word]
                else:
                    sentence_table[sent] += word_table[word]