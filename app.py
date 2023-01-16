from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():
   return render_template("index.html")

@app.route('/fetch_page')
def fetch_page():
   return render_template("fetch_page.html")

if __name__ == '__main__':
   app.run(debug=True)