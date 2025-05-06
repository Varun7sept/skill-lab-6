from flask import Flask, render_template

app = Flask(__name__)  # ✅ fixed typo from _name_ to __name__

@app.route('/')
def index():
    return render_template('index.html')  # First interactive page

@app.route('/page2')
def page2():
    return render_template('page2.html')  # Second interactive page

if __name__ == '__main__':  # ✅ fixed typo from _main_ to __main__
    app.run(debug=True)
