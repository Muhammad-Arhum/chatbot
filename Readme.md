# 🤖 Robofied Chatbot (Web-based)

A web-based chatbot built using Flask, Scikit-Learn, and Naive Bayes for basic text classification. The chatbot provides information about **Robofied's** services, including:

- Web Development
- Designing
- Cloud Computing (AWS)
- IoT
- Social Media Marketing
- AI & ML

---

## 📦 Project Structure

```plaintext
chatbot/
├── static/                  # Static files (CSS, JS)
│   ├── css/
│   │   └── style.css        # Styling for the chatbot interface
│   └── js/
│       └── app.js           # JavaScript handling frontend interactions
│
├── templates/
│   └── index.html           # Frontend (HTML template for the chatbot)
│
├── intents.json             # Contains chatbot training data (patterns and responses)
├── app.py                   # Flask backend and chatbot logic using Naive Bayes
├── requirements.txt         # List of required libraries
├── README.md                # Project documentation (this file)
└── .gitignore               # Git ignore file for environment files
```

🎯 Features

Text Classification: The chatbot uses a Naive Bayes classifier to respond to user inputs.
Machine Learning: Built with scikit-learn for text classification.
Web Interface: Interactive chat UI built with HTML, CSS, and JavaScript.
Intents Management: Intents are stored in a JSON file for easy modification.

🧩 Intents Format (intents.json)

The intents.json file is used to train the chatbot. It consists of patterns and responses for each tag.

🚀 Getting Started
1. Clone the Repository
```
git clone https://github.com/your-username/chatbot-web.git
cd chatbot-web
```
2. Create a Virtual Environment (Optional but Recommended)
```
python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate     # For Windows
```
3. Install Required Libraries
```
pip install -r requirements.txt
```

📦 Libraries Used

Flask – Web framework for Python
scikit-learn – Machine Learning library for training the Naive Bayes model
CountVectorizer – For text vectorization
MultinomialNB – Naive Bayes classifier for text classification

▶️ Running the Project
```
python app.py
```
The server will start at: http://127.0.0.1:5000

🖥️ How to Use the Chatbot?

Open the web browser and visit the link provided (http://127.0.0.1:5000).
Type a message in the chatbox.
The bot will respond based on the trained intents.

📈 Training the Model (How the Model Works)

Data Preprocessing:
    The chatbot reads intents.json and extracts patterns and tags.
Text Vectorization:
    CountVectorizer converts text data into numerical format for the model.
Model Training:
    MultinomialNB (Naive Bayes classifier) is trained on the vectorized data.
Prediction:
    The bot predicts the tag and responds with a matching response from the intents file.

💡 Contributing

Feel free to contribute by:

Adding more intents to intents.json
Improving the UI design
Optimizing the ML model

📞 Contact

Developer Name: Muhammad Arhum Naeem <br>
Email: engr.arhumnaeem@gmail.com <br>
Hire Me: https://www.upwork.com/freelancers/~01a323f7488996ce0d <br>
LinkedIn Profile: https://www.linkedin.com/in/me-arhumnaeem