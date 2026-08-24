from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/status', methods=['GET'])
def get_status():
    return jsonify({
        "status": "OPERATIONAL",
        "engine": "Python-Flask Runtime",
        "message": "Ndem-aDem Core Engine Linked Successfully"
    }), 200

if __name__ == '__main__':
    # Listen on all local container interfaces
    app.run(host='0.0.0.0', port=5000)
