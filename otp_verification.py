# import random
# import smtplib
# from email.mime.text import MIMEText

# def generate_otp(length=6):
#     otp = ''.join([str(random.randint(0, 9)) for _ in range(length)])
#     return otp

# def send_email(otp, recipient_email):
#     smtp_server = "smtp.gmail.com"
#     smtp_port = 587
#     sender_email = "madhur2k3@gmail.com"
#     sender_password = "yzyb fovy gebw ehzt"

#     subject = "Your OTP Code"
#     body = f"Your OTP code is {otp}. It will expire in 10 minutes."
#     msg = MIMEText(body)
#     msg['Subject'] = subject
#     msg['From'] = sender_email
#     msg['To'] = recipient_email

#     try:
#         with smtplib.SMTP(smtp_server, smtp_port) as server:
#             server.starttls()
#             server.login(sender_email, sender_password)
#             server.sendmail(sender_email, recipient_email, msg.as_string())
#             print("Email sent successfully.")
#     except Exception as e:
#         print(f"Failed to send email: {e}")

# def verify_otp(input_otp, actual_otp):
#     return input_otp == actual_otp

# if __name__ == "__main__":
#     recipient_email = input("Enter the recipient's email address: ")
#     otp = generate_otp()
#     send_email(otp, recipient_email)
#     input_otp = input("Enter the OTP you received: ")
#     if verify_otp(input_otp, otp):
#         print("OTP verified successfully!")
#     else:
#         print("Invalid OTP.")

from flask import Flask, render_template, request, jsonify
import random
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# Temporarily store the OTP for the session (this should be stored securely in a real system)
otp_storage = {}

# Function to generate OTP
def generate_otp(length=6):
    return ''.join([str(random.randint(0, 9)) for _ in range(length)])

# Function to send OTP email
def send_email(otp, recipient_email):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "madhur2k3@gmail.com"
    sender_password = "yzyb fovy gebw ehzt"

    subject = "Your OTP Code"
    body = f"Your OTP code is {otp}. It will expire in 10 minutes."
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
            print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Route to serve the HTML page
@app.route('/')
def home():
    return render_template('otp_verification.html')

# Route to handle sending OTP
@app.route('/send-otp', methods=['POST'])
def send_otp():
    email = request.form['email']
    otp = generate_otp()  # Generate the OTP
    otp_storage[email] = otp  # Store the OTP associated with the email
    send_email(otp, email)  # Send the OTP to the user's email
    return jsonify({'message': 'OTP sent to your email'})

# Route to verify the OTP
@app.route('/verify-otp', methods=['POST'])
def verify_otp():
    email = request.form['email']
    entered_otp = request.form['otp']

    # Check if the email is in the stored OTPs and the OTP matches
    if email in otp_storage and otp_storage[email] == entered_otp:
        return jsonify({'status': 'success', 'message': 'OTP verified successfully!'})
    else:
        return jsonify({'status': 'error', 'message': 'Invalid OTP. Please try again.'})

if __name__ == "__main__":
    app.run(debug=True)
