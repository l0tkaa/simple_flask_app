from flask import Flask, render_template, request

# create an instance of the Flask class
app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name'] # get the submitted name from teh form
    return f"Hello, {name}!"



if __name__ == "__main__":
    app.run(debug=True)