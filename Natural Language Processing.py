import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import spacy

# Download necessary resources for NLTK
nltk.download('punkt')
nltk.download('stopwords')

# Tokenize a text using NLTK
text = "This is a sample sentence."
tokens = word_tokenize(text)
print(tokens)

# Remove stopwords using NLTK
stop_words = set(stopwords.words('english'))
filtered_tokens = [token for token in tokens if token.lower() not in stop_words]
print(filtered_tokens)

# Perform named entity recognition using spaCy
nlp = spacy.load('en_core_web_sm')
doc = nlp("Apple is looking to buy a startup company.")
for entity in doc.ents:
print(entity.text, entity.label)
