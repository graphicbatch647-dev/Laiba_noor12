from flask import Flask, render_template, request

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Greet page
@app.route('/greet', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        name = request.form.get('name')
        return render_template('greet.html', name=name)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)