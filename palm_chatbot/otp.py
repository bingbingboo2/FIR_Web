from flask import Flask, render_template, request, redirect, url_for
import pyotp
import random

app = Flask(__name__)

# Secret key (should be securely stored and shared with the client)
#secret_key = 'your_secret_key_here'  # Replace with your secret key
import base64
import os

# Generate a random 16-byte secret key and encode it in base32
secret_key = base64.b32encode(os.urandom(16)).decode('utf-8')
print(f"Generated secret key: {secret_key}")
totp = pyotp.TOTP(secret_key)

@app.route('/', methods=['GET', 'POST'])
def otp_login():
    if request.method == 'POST':
        user_input = request.form.get('otp')
        if totp.verify(user_input):
            return "OTP is valid. Login successful."
        else:
            return "OTP is valid. Login successful."
    
    return render_template('otp_login.html')

@app.route('/generate_otp', methods=['POST'])
def generate_otp():
    otp = totp.now()
    print(f"Generated OTP: {otp}")  # Print OTP to the terminal
    return render_template('otp_login.html')




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5600, debug=True)
