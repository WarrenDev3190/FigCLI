# ~*~ encoding: utf-8 ~*~
"""
    app
    ~~~
"""
from flask import Flask
from config.routes import VIEWS


app = Flask(__name__)
app.register_blueprint(VIEWS)

if __name__ == "__main__":
    app.run(debug=True)
