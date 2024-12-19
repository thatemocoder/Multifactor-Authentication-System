

#final code
# import cv2
# from deepface import DeepFace
# import time

# # Load the reference image
# reference_img_path = "/Users/madhur/Desktop/Me/college/fourth year/project1/face_recognition/reference1.jpg"
# reference_img = cv2.imread(reference_img_path)

# # Initialize webcam
# cap = cv2.VideoCapture(0)

# if not cap.isOpened():
#     print("Error: Could not open webcam.")
#     exit()

# # Start timer
# start_time = time.time()

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         print("Error: Could not read frame.")
#         break

#     # Check elapsed time
#     elapsed_time = time.time() - start_time
#     if elapsed_time >= 6:
#         print("No match within 6 seconds. Turning off camera.")
#         break

#     # Try to verify the face in the current frame against the reference image
#     try:
#         result = DeepFace.verify(frame, reference_img)
#         face_match = result["verified"]
#     except Exception as e:
#         print("Error in face verification:", e)
#         face_match = False

#     # Display result on the frame
#     if face_match:
#         cv2.putText(frame, "MATCH! Turning off camera.", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#         cv2.imshow("Live Face Recognition", frame)
#         cv2.waitKey(2000)  # Display the message for 2 seconds
#         break  # Exit the loop to turn off the camera
#     else:
#         cv2.putText(frame, "NO MATCH!", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

#     # Show the frame
#     cv2.imshow("Live Face Recognition", frame)

#     # Press "q" to exit manually
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release resources
# cap.release()
# cv2.destroyAllWindows()


# from flask import Flask, render_template, Response
# import cv2
# from deepface import DeepFace
# import time

# app = Flask(__name__)

# # Load the reference image
# reference_img_path = "/Users/madhur/Desktop/Me/college/fourth year/project1/face_recognition/reference1.jpg"
# reference_img = cv2.imread(reference_img_path)

# # Initialize timer and match flag
# start_time = time.time()
# face_match = False

# def generate_frames():
#     global face_match, start_time

#     cap = cv2.VideoCapture(0)
#     if not cap.isOpened():
#         print("Error: Could not open webcam.")
#         return

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             print("Error: Could not read frame.")
#             break

#         # Check elapsed time
#         elapsed_time = time.time() - start_time
#         if elapsed_time >= 6:
#             print("No match within 6 seconds. Turning off camera.")
#             break

#         # Try to verify the face in the current frame against the reference image
#         try:
#             result = DeepFace.verify(frame, reference_img)
#             face_match = result["verified"]
#         except Exception as e:
#             print("Error in face verification:", e)
#             face_match = False

#         # Display result on the frame
#         if face_match:
#             cv2.putText(frame, "MATCH! Turning off camera.", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#             _, buffer = cv2.imencode('.jpg', frame)
#             frame = buffer.tobytes()
#             yield (b'--frame\r\n'
#                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
#             time.sleep(2)  # Display the message for 2 seconds
#             break  # Exit the loop to turn off the camera
#         else:
#             cv2.putText(frame, "NO MATCH!", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

#         # Encode frame
#         _, buffer = cv2.imencode('.jpg', frame)
#         frame = buffer.tobytes()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

#     cap.release()

# @app.route('/')
# def index():
#     return render_template('face_recognition.html')

# @app.route('/video_feed')
# def video_feed():
#     return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# if __name__ == '__main__':
#     app.run(debug=True)


# import cv2
# from deepface import DeepFace
# import time

# # Load the reference image
# reference_img_path = "/Users/madhur/Desktop/Me/college/fourth year/project1/face_recognition/reference2.jpg"
# reference_img = cv2.imread(reference_img_path)

# # Initialize timer and match flag
# start_time = time.time()
# face_match = False

# # Open webcam
# cap = cv2.VideoCapture(0)
# if not cap.isOpened():
#     print("Error: Could not open webcam.")
#     exit()

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         print("Error: Could not read frame.")
#         break

#     # Check elapsed time
#     elapsed_time = time.time() - start_time
#     if elapsed_time >= 10:  # Keep camera on for 10 seconds
#         print("No match within 10 seconds. Turning off camera.")
#         break

#     # Try to verify the face in the current frame against the reference image
#     try:
#         result = DeepFace.verify(frame, reference_img, enforce_detection=False)
#         face_match = result["verified"]
#         print("DeepFace Result:", result)  # Debug: Display result details
#     except Exception as e:
#         print("Error in face verification:", e)
#         face_match = False

#     # Display result on the frame
#     if face_match:
#         cv2.putText(frame, "MATCH! Turning off camera.", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#         print("Face matched. Turning off camera.")
#         cv2.imshow('Face Recognition', frame)
#         time.sleep(10)  # Display the message for 2 seconds
#         break
#     else:
#         cv2.putText(frame, "NO MATCH!", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

#     # Display the frame
#     cv2.imshow('Face Recognition', frame)

#     # Exit if 'q' is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         print("User terminated the program.")
#         break

# # Release resources
# cap.release()
# cv2.destroyAllWindows()

import cv2
from deepface import DeepFace

# Load the reference image
reference_img_path = "/Users/madhur/Desktop/Me/college/fourth year/project1/face_recognition/reference2.jpg"
reference_img = cv2.imread(reference_img_path)

# Open webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    # Try to verify the face in the current frame against the reference image
    try:
        result = DeepFace.verify(frame, reference_img, enforce_detection=False)
        face_match = result["verified"]
        print("DeepFace Result:", result)  # Debug: Display result details
    except Exception as e:
        print("Error in face verification:", e)
        face_match = False

    # Display result on the frame
    if face_match:
        cv2.putText(frame, "MATCH!", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    else:
        cv2.putText(frame, "NO MATCH!", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Display the frame
    cv2.imshow('Face Recognition', frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("User terminated the program.")
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
