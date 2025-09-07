# URL-Shortner

A lightweight and efficient URL Shortener that converts long, cumbersome URLs into short, easy-to-share links. Built with Python (3.8), Flask (for the web server and routing) and JSON (for storage)

##  Features
- Shortens any valid URL into a unique ID (<12 ASCII characters).
- Stores shortened URLs and their mappings in a JSON file (urls.json).
- Redirects users to the original URL when a shortened link is visited.
- Counts how many URLs have been shortened so far.
- Protects against invalid URLs.


##  Table of Contents
- [Installation](#installation)  
- [Usage](#usage)  
- [API](#api) *(if applicable)*  
- [Example](#example)  
- [Contributing](#contributing)  
- [License](#license)


##  Installation

1. Clone this repository:  
   ```bash
   git clone https://github.com/maciriase26/URL-Shortner.git
   cd URL-Shortner

2. Install dependencies
    Create a virtual environment and install Flask:
    python -m venv venv
    # macOS/Linux
    source venv/bin/activate
    # Windows
    venv\Scripts\activate
    
    pip install flask

3. Run the app
    python app.py
    
    (You should see- * Running on http://127.0.0.1:5000)

4. Open in Browser or Follow Link
   
