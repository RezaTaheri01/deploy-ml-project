# jovian.com/biraj/deploying-a-machine-learning-model
# https://github.com/KalyanM45/Spam-Email-Detection
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load tokenizer and model
tokenizer = pickle.load(open('models/features.pkl', 'rb'))
model = pickle.load(open('models/stack_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        text_input = request.form.get("emailContent", "").strip()
        if not text_input:
            return render_template("index.html", text="No input provided.")

        tokenized = text_tokenizer([text_input])
        prediction = predict_spam(tokenized)

        result = "This email is spam." if prediction[0] == 0 else "This email is not spam."
        return render_template("index.html", text=f"{result}\n\n{text_input}")

    except Exception as e:
        return f"Error: {str(e)}", 500



def text_tokenizer(text):
    return tokenizer.transform(text)

def predict_spam(tokenized_text):
    return model.predict(tokenized_text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8000)