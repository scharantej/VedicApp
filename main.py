
# Import necessary modules
from flask import Flask, render_template

# Create a Flask application
app = Flask(__name__)

# Define the routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sutras')
def sutras():
    return render_template('sutras.html')

@app.route('/sutras/<sutra_name>')
def specific_sutra(sutra_name):
    return render_template('sutra.html', sutra_name=sutra_name)

@app.route('/techniques')
def techniques():
    return render_template('techniques.html')

@app.route('/techniques/<technique_name>')
def specific_technique(technique_name):
    return render_template('technique.html', technique_name=technique_name)

@app.route('/examples')
def examples():
    return render_template('examples.html')

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
