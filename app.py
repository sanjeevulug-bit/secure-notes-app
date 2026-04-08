from flask import Flask, request, redirect
import os

app = Flask(__name__)

notes = []

@app.route('/')
def home():
    return open("index.html").read().replace("{{notes}}", "<br>".join(notes))

@app.route('/add', methods=['POST'])
def add_note():
    note = request.form['note']
    notes.append(note)
    return redirect('/')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)