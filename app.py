from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Konfiguracja bazy danych PostgreSQL z Render
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")  # Pobieranie URL bazy z Render
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model użytkownika w bazie danych
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# Tworzenie tabeli w bazie
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return "Hello, World! Aplikacja działa!"

if __name__ == "__main__":
    app.run()