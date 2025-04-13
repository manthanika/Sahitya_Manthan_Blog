from flask import Flask, request, jsonify, render_template
import csv
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

app = Flask(__name__)

CSV_FILE = 'feedback.csv'

# Create CSV file with headers if it doesn't exist
def initialize_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Email', 'Message', 'Timestamp'])

# Save form data to CSV
def save_to_csv(name, email, message):
    with open(CSV_FILE, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([name, email, message, datetime.now().strftime("%Y-%m-%d %H:%M:%S")])

# Send email using Gmail SMTP
def send_email(name, email, message):
    sender_email = "manthanikaa@gmail.com"
    receiver_email = "manthanikaa@gmail.com"
    password = "zhtg hrme peuj fbph"  # App password, should be secured

    subject = "New Feedback Received"
    body = f"Name: {name}\nEmail: {email}\nMessage:\n{message}"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
    except Exception as e:
        print(f"Error sending email: {e}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    try:
        save_to_csv(name, email, message)
        send_email(name, email, message)
        return jsonify({'status': 'success', 'message': 'Thank you for your feedback!'})
    except Exception as e:
        print("Error:", e)
        return jsonify({'status': 'error', 'message': 'Failed to submit feedback.'})

if __name__ == '__main__':
    initialize_csv()
    app.run(debug=True)
