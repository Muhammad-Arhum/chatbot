import json

from flask import Flask, jsonify, render_template, request
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

app = Flask(__name__)

# Load intents
with open('intents.json', 'r') as file:
    data = json.load(file)

patterns = []
labels = []
for intent in data['intents']:
    for pattern in intent['patterns']:
        patterns.append(pattern)
        labels.append(intent['tag'])

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(patterns)

model = MultinomialNB()
model.fit(X, labels)

def get_response(user_input):
    user_input_vectorized = vectorizer.transform([user_input])
    tag = model.predict(user_input_vectorized)[0]
    for intent in data['intents']:
        if intent['tag'] == tag:
            return intent['responses'][0]
    return "I'm not sure how to respond to that."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_chat_response():
    user_input = request.json['message']
    response = get_response(user_input)
    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(debug=True)
