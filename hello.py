from flask import Flask
from flask import render_template
import time

app = Flask(__name__, static_url_path='/static/')

@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/home')
def home():
    return app.send_static_file('index.html')

@app.route('/time')
def what_time():
    current_time = time.strftime("%c")
    return render_template('time.html', current_time=current_time)

@app.route('/<path:path>')
def send_static(path):
    return app.send_static_file(path)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
