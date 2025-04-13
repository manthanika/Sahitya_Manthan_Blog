from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbx7rwKG_V2XTP0tVuCVjHWtwlyb3dM_k3GnzvSPNQVEB--yOy_1cXYUodtBK4TuXzMIUA/exec"

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    data = request.get_json()
    
    response = requests.post(
        GOOGLE_SCRIPT_URL,
        json=data,
        headers={"Content-Type": "application/json"}
    )

    return jsonify({"google_response": response.text})

if __name__ == '__main__':
    app.run(debug=True)
