# app.py
import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    secret_val = os.environ.get("ADMIN_SECRET")
    if secret_val:
        return f"Hello Admin. You've configured the app correctly. (secret={secret_val})\n"
    return "Hello World\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
