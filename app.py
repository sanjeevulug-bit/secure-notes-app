from flask import Flask, request, redirect
import html

app = Flask(__name__)

notes = []

@app.route('/')
def home():
    safe_notes = [html.escape(note) for note in notes]
    return open("index.html").read().replace("{{notes}}", "<br>".join(safe_notes))

@app.route('/add', methods=['POST'])
def add_note():
    note = request.form['note']

    # Basic validation
    if len(note) > 100:
        return "Note too long!"

    notes.append(note)
    return redirect('/')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)