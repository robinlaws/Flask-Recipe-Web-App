from flask import Flask
from website import create_app

def app1():
    app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
