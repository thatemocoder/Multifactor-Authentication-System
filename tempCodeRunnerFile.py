from flask import Flask, request, jsonify, render_template
import face_recognition
import os
import numpy as np
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Paths
KNOWN_FACES_FOLDER = 'known_faces'
UPLOAD_FOLDER = 'uploads'

# Load known faces
known_face_encodings = []
known_face_names = []

folder_path = "/Users/madhur/Desktop/Me/college/fourth year/project1/face_recognition/known_faces"

def load_known_faces(folder_path):
    global known_face_encodings, known_face_names
    known_face_encodings = []
    known_face_names = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(folder_path, filename)
            image = face_recognition.load_image_file(image_path)
            face_encodings = face_recognition.face_encodings(image)
            if face_encodings:  # Check if at least one face encoding is found
                face_encoding = face_encodings[0]
                name = os.path.splitext(filename)[0]
                known_face_encodings.append(face_encoding)
                known_face_names.append(name)

# Ensure upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

load_known_faces(KNOWN_FACES_FOLDER)

@app.route('/')
def index():
    return render_template('face_recognition.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)

        # Load uploaded image and find faces
        uploaded_image = face_recognition.load_image_file(file_path)
        uploaded_face_encodings = face_recognition.face_encodings(uploaded_image)

        results = []
        for face_encoding in uploaded_face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # If a match was found, use the first one
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            results.append(name)

        return jsonify({'names': results})

if __name__ == "__main__":
    app.run(debug=True)
