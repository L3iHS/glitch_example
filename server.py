import os

from flask import Flask
from dotenv import load_dotenv


load_dotenv(override=True)
app = Flask(__name__)


@app.route("/")
def index():
    return "Привет от приложения Flask (Илья)"


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)