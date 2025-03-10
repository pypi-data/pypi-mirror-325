import numpy as np
from gensim.models import Word2Vec
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import joblib


# Preprocessing function
def preprocess_text(text):
    """
    Preprocesses the input text by converting it to lowercase, removing punctuation, tokenizing, and removing stopwords.
    Args:
        text (str): The input text to be preprocessed.
    Returns:
        list: A list of tokens after preprocessing.
    """
    # Load the trained Word2Vec model and Extra Trees Classifier model


    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english')).union(ENGLISH_STOP_WORDS)
    tokens = [word for word in tokens if word not in stop_words]
    return tokens

# Function to get message embedding
def get_message_embedding(message, model):
    """
    Generate the embedding vector for a given message using a pre-trained word embedding model.
    Args:
        message (str): The input message to be embedded.
        model (gensim.models.Word2Vec): The pre-trained word embedding model.
    Returns:
        numpy.ndarray: The embedding vector of the input message. If none of the words in the message
                       are found in the model's vocabulary, returns a zero vector of the model's vector size.
    """

    tokens = preprocess_text(message)
    vectors = [model.wv[word] for word in tokens if word in model.wv]
    if vectors:
        return np.mean(vectors, axis=0)
    else:
        return np.zeros(model.vector_size)

def predict(message):
    """
    Predicts whether a given message is spam or not and returns the prediction along with the confidence level.
    Args:
        message (str): The message to be classified.
    Returns:
        tuple: A tuple containing:
            - prediction (string): The predicted class ('scam' or 'trust').
            - confidence (float): The confidence level of the prediction.
    """
    import os
    # Load the trained Word2Vec model and Extra Trees Classifier model
    base_path = os.path.dirname(os.path.abspath(__file__))
    word2vec_model_path = os.path.join(base_path, "word2vec.model")
    extra_trees_model_path = os.path.join(base_path, "best_logistic_regression_model.pkl")

    word2vec_model = Word2Vec.load(word2vec_model_path)
    extra_trees_model = joblib.load(extra_trees_model_path)

    nltk.download('punkt')
    nltk.download('stopwords')
    # Generate embedding for the message
    embedding = get_message_embedding(message, word2vec_model)

    # Make prediction and get probabilities using Extra Trees Classifier model
    prediction = extra_trees_model.predict([embedding])[0]
    probabilities = extra_trees_model.predict_proba([embedding])[0]
    
    confidence = max(probabilities)

    # Return the prediction and confidence
    return prediction, confidence


if __name__ == '__main__':
    sample_message = "Congratulations! You've won a $1000 Walmart gift card. Go to http://bit.ly/123456 to claim now."
    prediction, confidence = predict(sample_message)
    print(f"Message: {sample_message}")
    print(f"Prediction: { prediction }")
    print(f"Confidence: {confidence:.2f}")
