from flask import Flask, render_template, request #add render_template to adding list
from vsearch import search4letters #just testing

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'

@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    the_title = title 
    the_results = results search4letters
    
    return render_template('results.html',
                           the_title='Here are your results:')


@app.route('/entry') # Создать новый URL
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letters my webpage!')
app.run(debug=True)
