from flask import Flask, render_template, request #add render_template to adding list
from vsearch import search4letters 

app = Flask(__name__)

#def hello() -> '302':
 #   return redirect('/entry')

@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here your results: '
    results = str(search4letters(phrase, letters))
    return render_template('results.html',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_title=title,
                           the_results=results,)

@app.route('/')
@app.route('/entry') # Создать новый URL
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letters MY OWN webpage!')
app.run(debug=True)
