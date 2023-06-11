import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import precision_score


class Model:
    def __init__(self, news_input):
        self.news_input = news_input

    def prediction(self):
        # Load the dataset
        df = pd.read_csv('fake_news_detector/Dataset.csv')

        # Split the data into text and label columns
        X = df['News']
        y = df['Label']

        # Convert the text data into numerical vectors
        vectorizer = TfidfVectorizer()
        X_vectors = vectorizer.fit_transform(X)

        # Define and train a machine learning model
        model = MultinomialNB()
        model.fit(X_vectors, y)

        # Convert the input into a numerical vector using the same vectorizer
        news_vector = vectorizer.transform([self.news_input])

        # Predict the label of the input
        label = model.predict(news_vector)[0]

        # Calculate the accuracy of the prediction
        y_pred = model.predict(X_vectors)
        accuracy = sum(y == y_pred) / len(y_pred)
        precision = precision_score(y, y_pred, pos_label='Real')

        # Print the predicted label, accuracy, and precision
        print('Predicted label:', label)
        print('Accuracy:', accuracy)
        print('Precision:', precision)

        # Return the predicted label, accuracy, and precision
        return label, accuracy, precision
