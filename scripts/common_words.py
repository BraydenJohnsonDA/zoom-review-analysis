import pandas as pd
import nltk
from collections import Counter
import string
from nltk.corpus import stopwords
from nltk import pos_tag, word_tokenize

# Download necessary NLTK datasets (only runs once)
nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")
nltk.download("stopwords")

# Load the Apple App Store review dataset
df = pd.read_csv("apple_app_reviews_raw.csv")

# Join all review text into one large string
text = " ".join(str(t) for t in df["text"] if isinstance(t, str))

# Convert to lowercase and remove punctuation
text = text.lower().translate(str.maketrans('', '', string.punctuation))

# Tokenize the cleaned text
tokens = word_tokenize(text)

# Tag each token with its part of speech
tagged = pos_tag(tokens)

# Keep only nouns and adjectives (useful for sentiment & topics)
valid_tags = ["NN", "NNS", "NNP", "JJ", "JJR", "JJS"]

# Extend stopwords to exclude common or unhelpful words
custom_stopwords = set(stopwords.words("english")).union({
    "app", "get", "got", "like", "use", "used", "using", "one", "really", "would",
    "also", "still", "even", "make", "much", "can", "could", "thing", "just",
    "well", "time", "way", "ever", "ive", "dont", "doesnt", "cant", "wont",
    "know", "say", "see", "something", "lot", "every", "everything", "zoom",
})

# Filter tokens based on part-of-speech and remove stopwords
filtered = [
    word for word, tag in tagged
    if tag in valid_tags and word not in custom_stopwords and len(word) > 2
]

# Count and display the 50 most common filtered words
counts = Counter(filtered)
for word, count in counts.most_common(50):
    print(f"{word}: {count}")
