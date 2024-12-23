from flask import Flask, render_template

app = Flask(name)

# Маршрут для главной страницы
@app.route('/')
def home():
    return render_template('index.html')

if name == 'main':
    app.run(debug=True)
