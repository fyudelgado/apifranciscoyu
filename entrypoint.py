import os
from app import create_app
from flask import Flask

app = Flask(__name__)

settings_module = os.getenv('APP_SETTINGS_MODULE')
app = create_app(settings_module)


if __name__ == '__main__':
    app.run(debug=True)
