import string

import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from collections import Counter

# For future usage
import nltk
# nltk.download('wordnet')
# nltk.download('stopwords')
# nltk.download('averaged_perceptron_tagger')

global terms

# Storing tokenized data
class ArticleData:
    def __init__(self, header, text):
        self.header = header
        self.text = text
        self.converted_tokens = None
        self.tfidf_calculations = None
        self.most_common_words = None

        self.convert_text_to_tags()

    def __str__(self):
        if self.tfidf_calculations is not None:
            output = f"{self.header}:\n"
            for word in self.most_common_words[:-1]:
                output += (word[0] + " ")
            output += self.most_common_words[-1][0]
            return output
        else:
            return "Article has not been prepared for content review!"

    def convert_text_to_tags(self):
        # Tokenization
        word_tokens = word_tokenize(self.text.lower())

        # Lematization
        lemmatizer = WordNetLemmatizer()
        lemmatizered_text = [lemmatizer.lemmatize(w) for w in word_tokens]

        # Reducing punctation and stopwords
        stopwords_set = stopwords.words('english')
        punctuation_set = list(string.punctuation)
        reduced_text = [w for w in lemmatizered_text if w not in stopwords_set + punctuation_set]

        # Reducing to only nouns
        only_nouns = [x for x in reduced_text if nltk.pos_tag([x])[0][1] == "NN"]

        output_counter = Counter(only_nouns)
        output_counter = output_counter.most_common()
        # output_counter = self.sort_equal_values(output_counter, len(output_counter) - 1)

        output_list = []
        for word in output_counter:
            for i in range(word[1]):
                output_list.append(word[0])

        self.converted_tokens = output_list


    def calc_most_common_words(self, terms):
        if self.tfidf_calculations is not None:
            df = pd.DataFrame(self.tfidf_calculations.toarray())
            df2 = df.transpose().sort_values(by=0, ascending=False).reset_index()

            self.most_common_words = list()
            for i in range(len(df2)):
                word = terms[int(df2.iloc[i]['index'])]
                value = float(df2.iloc[i][0])
                self.most_common_words.append(tuple([word, value]))
            self.most_common_words.sort(key=lambda words: (words[1], words[0]), reverse=True)
            self.most_common_words = self.most_common_words[:5]
        else:
            return "Article has not been filtered by vectorizer!"
