from flask import Flask

app = Flask(__name__)

@app.route("/") ## / means its for the home page
def home():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)

## Run this App : In terminal ---> python app.py    