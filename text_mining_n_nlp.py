import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download necessary resources
nltk.download('punkt')
nltk.download('stopwords')

# Load the text data
text = "This is a sample sentence for text mining and NLP."

# Tokenize the text
tokens = word_tokenize(text)

# Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_tokens = [token for token in tokens if token.lower() not in stop_words]

# Perform stemming or lemmatization
stemmer = nltk.PorterStemmer()
lemmatizer = nltk.WordNetLemmatizer()
stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]
lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]

# Perform other NLP tasks (e.g., sentiment analysis, named entity recognition, etc.)
# ... code for other NLP tasks using NLTK or other libraries ...

# Print the results
print("Original tokens:", tokens)
print("Filtered tokens:", filtered_tokens)
print("Stemmed tokens:", stemmed_tokens)
print("Lemmatized tokens:", lemmatized_tokens)
