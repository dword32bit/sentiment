from flask import Flask, render_template, request
from tweets_analysis import analyze_tweets

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        query = request.form['query']
        tweets, sentiment_scores = analyze_tweets(query)
        return render_template('index.html', query=query, tweets=tweets, sentiment_scores=sentiment_scores)

if __name__ == "__main__":
    app.run(debug=True)
