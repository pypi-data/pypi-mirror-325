from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def get_time():
    """ Returns the current server time in JSON format. """
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return jsonify({"current_time": current_time})

def main():
    app.run(host='0.0.0.0', port=8080, debug=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
