from flask import Flask, request, redirect, render_template_string, jsonify
import json, os, random, string
from urllib.parse import urlparse
#Tests- 

app = Flask(__name__)
DATA_FILE = "urls.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def generate_short_id(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def is_valid_url(url):
    parsed = urlparse(url)
    return parsed.scheme in ("http", "https") and parsed.netloc

PAGE_TEMPLATE = """
<!DOCTYPE html>
<html>
<head><title>URL Shortener CS230</title></head>
<body>
  <h2>URL Shortener</h2>
  <form method="POST">
    <input type="text" name="url" placeholder="Enter full URL" size="50">
    <button type="submit">Shorten</button>
  </form>
  <p>{{ message|safe }}</p>
  <p><a href="/count">View total shortened</a></p>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        url = request.form.get("url", "")
        if not is_valid_url(url):
            message = " Invalid URL must be https:// or http://"
        else:
            data = load_data()
            short_id = generate_short_id()
            while short_id in data:
                short_id = generate_short_id()
            data[short_id] = url
            save_data(data)
            short_url = f"http://127.0.0.1:5000/{short_id}"
            message = f" <a href='{short_url}'>{short_url}</a>"
    return render_template_string(PAGE_TEMPLATE, message=message)

@app.route("/<short_id>")
def redirect_to_url(short_id):
    data = load_data()
    original = data.get(short_id)

    if original:
        print(f"Redirecting {short_id} → {original}") 
        if not original.startswith(("http://", "https://")):
            original = "http://" + original
        return redirect(original, code=302)

    return "ERROR: Shortened URL not found", 404

@app.route("/count")
def count():
    return f"Total URLs shortened: {len(load_data())}"

if __name__ == "__main__":
    app.run(debug=True)
