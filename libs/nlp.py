import re
from collections import Counter

import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download("punkt")
nltk.download("wordnet")
nltk.download("omw-1.4")
nltk.download("stopwords")
nltk.download("averaged_perceptron_tagger")

def preprocessing(text):
    text = re.sub("[^-9A-Za-z ]", "", text).lower()
    stop = stopwords.words("indonesian")
    tokens = [
        word for word in (token for token in word_tokenize(text)) if word not in stop
    ]
    return tokens