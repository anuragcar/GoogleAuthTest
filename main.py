from flask import Flask, render_template

app = Flask(name)

@app.route('/')
def start():
    return render_template('loginPage.html', message='Hello-World', othera='whatever')

if name == 'main':
    app.run(debug=True)