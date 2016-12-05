from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
import nltk
nltk.download('punkt')

from nltk import word_tokenize,sent_tokenize
train = [
    ('I love this hotdog.', 'pos'),
    ('This is an amazing magazine!', 'pos'),
    ('I feel very good about these compots.', 'pos'),
    ('This is my best laboratory work.', 'pos'),
    ("What an awesome view", 'pos'),
    ('I do not like this class', 'neg'),
    ('I am tired of this classmates.', 'neg'),
    ("I can't deal with this", 'neg'),
    ('He is my sworn enemy!', 'neg'),
    ('My colleague is horrible.', 'neg')
]
test = [
    ('The compot was good.', 'pos'),
    ('I do not enjoy my job', 'neg'),
    ("I ain't feeling dandy today.", 'neg'),
    ("I feel amazing!", 'pos'),
    ('Eldos is a friend of mine.', 'pos'),
    ("I can't believe I'm doing this.", 'neg')
]

cl = NaiveBayesClassifier(train)

# Classify some text
print(cl.classify("Their hotdogs are amazing."))  # "pos"
print(cl.classify("I don't like their pizza."))   # "neg"

# Classify a TextBlob
blob = TextBlob("The compot was amazing. But the hangover was horrible. "
                "My teacher was not pleased.", classifier=cl)
print(blob)
print(blob.classify())

for sentence in blob.sentences:
    print(sentence)
    print(sentence.classify())

# Compute accuracy
print("Accuracy: {0}".format(cl.accuracy(test)))

# Show 5 most informative features
cl.show_informative_features(5)