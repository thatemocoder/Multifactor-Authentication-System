# import sounddevice as sd
# from scipy.io.wavfile import write
# import speech_recognition as sr

# def record_audio(filename, duration=5, fs=44100):
#     """
#     Records audio from the microphone and saves it as a WAV file.
#     """
#     print("Please read the text aloud: 'Welcome to my project'")
#     print("Recording...")
#     audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
#     sd.wait()  # Wait until the recording is finished
#     write(filename, fs, audio)  # Save as WAV file
#     print("Recording complete!")

# def verify_speech_from_file(filename, expected_text):
#     """
#     Verifies if the spoken words in the WAV file match the expected text.
#     """
#     recognizer = sr.Recognizer()
#     with sr.AudioFile(filename) as source:
#         audio_data = recognizer.record(source)
#         try:
#             # Recognize speech using Google's Speech Recognition
#             speech_text = recognizer.recognize_google(audio_data)
#             print(f"You said: {speech_text}")
#             if speech_text.lower() == expected_text.lower():
#                 print("Verification successful! Text matches.")
#             else:
#                 print("Verification failed. Text does not match.")
#         except sr.UnknownValueError:
#             print("Sorry, I could not understand the audio.")
#         except sr.RequestError as e:
#             print(f"Could not request results; {e}")

# # Define the text to verify
# text_to_verify = "Welcome to my project"

# # Record the user's speech and save it as 'output.wav'
# record_audio("output.wav")

# # Verify if the user's speech matches the text
# verify_speech_from_file("output.wav", text_to_verify)


from flask import Flask, render_template, request, jsonify
import sounddevice as sd
from scipy.io.wavfile import write
import speech_recognition as sr
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('speech.html')

@app.route('/record', methods=['POST'])
def record_audio():
    """
    Records audio and saves it as 'output.wav'.
    """
    try:
        filename = "output.wav"
        duration = 5  # seconds
        fs = 44100  # Sample rate
        print("Recording audio...")
        audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
        sd.wait()  # Wait until recording is finished
        write(filename, fs, audio)
        print("Recording complete!")
        return jsonify({"status": "success"})
    except Exception as e:
        print(f"Error during recording: {e}")
        return jsonify({"status": "error", "message": str(e)})

@app.route('/verify', methods=['POST'])
def verify_speech():
    """
    Verifies the user's speech matches the expected text.
    """
    expected_text = "Welcome to my project"
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile('output.wav') as source:
            audio_data = recognizer.record(source)
            speech_text = recognizer.recognize_google(audio_data)
            print(f"Recognized speech: {speech_text}")
            if speech_text.lower() == expected_text.lower():
                result = "Verification successful! Text matches."
            else:
                result = "Verification failed. Text does not match."
    except sr.UnknownValueError:
        result = "Sorry, I could not understand the audio."
    except sr.RequestError as e:
        result = f"Could not request results; {e}"
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
