# SMS Spam Detection
This project is an SMS Spam Detection application built using Flask, Word2Vec, and Extra Trees Classifier. The application provides an API endpoint to predict whether a given SMS message is spam or not.

## Features

- Preprocesses text data by tokenizing, removing punctuation, and filtering out stop words.
- Generates message embeddings using a pre-trained Word2Vec model.
- Predicts whether a message is spam or not using an Extra Trees Classifier model.
- Provides a web interface for users to input messages and get predictions.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/amintaheri23/sms-spam-detection.git
    cd sms-spam-detection
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Download NLTK data:
    ```sh
    python -m nltk.downloader punkt stopwords
    ```

## Usage
you can use the `predict` function directly in your code:
    ```python
    from sms_spam_detection import predict

    message = "Congratulations! You've won a free ticket to the Bahamas!"
    prediction = predict(message)
    print(prediction)
    ```
## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [Gensim](https://radimrehurek.com/gensim/)
- [scikit-learn](https://scikit-learn.org/)
- [NLTK](https://www.nltk.org/)
- [Waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/)

## Author

Created by Amin Taheri - [GitHub](https://github.com/amintaheri23)
