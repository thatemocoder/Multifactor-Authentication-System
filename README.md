# 🔐 Multifactor Authentication System

This project implements a multifactor authentication (MFA) system to enhance security by requiring multiple forms of verification. It combines facial recognition, speech recognition, and one-time password (OTP) verification to authenticate users.

---

### 📚 Project Overview

The system operates through a multi-step authentication process:

1. **Login Page**: Users enter their username and password.
2. **Face Recognition**: Upon successful login, the system captures the user's face using a webcam and compares it with stored facial data to verify identity.
3. **Speech Authentication**: Users are prompted to speak a predefined passphrase. The system processes the audio input to confirm the user's identity.
4. **OTP Verification**: A one-time password is sent to the user's registered email or phone number. The user must enter this OTP to complete the authentication process.

This layered approach ensures robust security by combining something the user knows (password), something the user has (OTP), and something the user is (biometric data).

---

### 🗂️ Repository Structure

- **`login.html`**: Frontend interface for user login.
- **`login.py`**: Backend script to handle user authentication.
- **`face_recognition.html`**: Interface for facial recognition setup.
- **`face_recognition_project.py`**: Script for capturing and processing facial data.
- **`otp_verification.html`**: Interface for OTP input.
- **`otp_verification.py`**: Script for generating and verifying OTPs.
- **`speech.html`**: Interface for speech authentication.
- **`speech.css`**: Styling for the speech authentication page.
- **`text_to_speech.py`**: Script for converting text to speech prompts.
- **`webcam.py`**: Script for accessing and processing webcam input.
- **`test_script.py`**: Utility script for testing components.
- **`python_requirements.txt`**: List of required Python libraries.

---

### 🛠️ Technologies Used

- **Frontend**: HTML, CSS
- **Backend**: Python
- **Libraries**:
  - OpenCV (for face recognition)
  - SpeechRecognition (for speech authentication)
  - pyttsx3 (for text-to-speech)
  - Twilio (for OTP generation and sending)
  - Flask (for web framework)

---

### 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/thatemocoder/Multifactor-Authentication-System.git
cd Multifactor-Authentication-System
```
2. Install required Python libraries:

```bash
pip install -r python_requirements.txt
```
3. Run the application:

```bash
python login.py
```
4. Access the application in your web browser at http://127.0.0.1:5000.
