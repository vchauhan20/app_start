from flask import Flask,request,render_template
from model import create_model,preprocess_data
from tensorflow.keras.preprocessing.text import Tokenizer
from joblib import load

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html",positive =0 , negative =0)


if __name__ == '__main__':
    app.run(debug=True)
