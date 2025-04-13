from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace this with your Apps Script deployment URL
GOOGLE_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbzplB3EQDCcbmyLkE3xcz5IE8odU4_FcRNSIcmrBBwy_skizYHlOLbLJngpuKkZqV2ZwA/exec'

@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    data = request.json

    response = requests.post(GOOGLE_SCRIPT_URL, json={
        'name': data.get('name'),
        'email': data.get('email'),
        'message': data.get('message')
    })

    if response.status_code == 200:
        return jsonify({"status": "success"}), 200
    else:
        return jsonify({"status": "failed", "error": response.text}), 500

if __name__ == '__main__':
    app.run(debug=True)
