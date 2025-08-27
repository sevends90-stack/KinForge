from flask import Flask, render_template_string, request, redirect
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS entries (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    message TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def insert_entry(name, message):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("INSERT INTO entries (name, message) VALUES (?, ?)", (name, message))
    conn.commit()
    conn.close()

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>KinForge Portal</title>
  <style>
    body {
      font-family: 'Segoe UI', sans-serif;
      background: #f0f2f5;
      margin: 0;
      padding: 2em;
    }
    .container {
      background: white;
      padding: 2em;
      max-width: 600px;
      margin: auto;
      border-radius: 8px;
      box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }
    input, textarea {
      width: 100%;
      padding: 1em;
      margin-top: 1em;
      border: 1px solid #ccc;
      border-radius: 4px;
    }
    button {
      background: #007BFF;
      color: white;
      padding: 1em 2em;
      border: none;
      border-radius: 4px;
      margin-top: 1em;
      cursor: pointer;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Welcome to KinForge</h1>
    <form method="POST">
      <input type="text" name="name" placeholder="Your Name" required>
      <textarea name="message" placeholder="Your Message" required></textarea>
      <button type="submit">Submit</button>
    </form>
    {% if name %}
      <p><strong>Received from {{ name }}:</strong> {{ message }}</p>
    {% endif %}
  </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    name = None
    message = None
    if request.method == "POST":
        name = request.form.get("name")
        message = request.form.get("message")
        insert_entry(name, message)
        return redirect("/")
    return render_template_string(HTML_TEMPLATE, name=name, message=message)

if __name__ == "__main__":
    init_db()
    app.run(debug=False, port=5000)from flask import Flask, render_template_string, request, redirect
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS entries (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    message TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def insert_entry(name, message):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("INSERT INTO entries (name, message) VALUES (?, ?)", (name, message))
    conn.commit()
    conn.close()

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>KinForge Portal</title>
  <style>
    body {
      font-family: 'Segoe UI', sans-serif;
      background: #f0f2f5;
      margin: 0;
      padding: 2em;
    }
    .container {
      background: white;
      padding: 2em;
      max-width: 600px;
      margin: auto;
      border-radius: 8px;
      box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }
    input, textarea {
      width: 100%;
      padding: 1em;
      margin-top: 1em;
      border: 1px solid #ccc;
      border-radius: 4px;
    }
    button {
      background: #007BFF;
      color: white;
      padding: 1em 2em;
      border: none;
      border-radius: 4px;
      margin-top: 1em;
      cursor: pointer;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Welcome to KinForge</h1>
    <form method="POST">
      <input type="text" name="name" placeholder="Your Name" required>
      <textarea name="message" placeholder="Your Message" required></textarea>
      <button type="submit">Submit</button>
    </form>
    {% if name %}
      <p><strong>Received from {{ name }}:</strong> {{ message }}</p>
    {% endif %}
  </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    name = None
    message = None
    if request.method == "POST":
        name = request.form.get("name")
        message = request.form.get("message")
        insert_entry(name, message)
        return redirect("/")
    return render_template_string(HTML_TEMPLATE, name=name, message=message)

if __name__ == "__main__":
    init_db()
    app.run(debug=False, port=5000) 

