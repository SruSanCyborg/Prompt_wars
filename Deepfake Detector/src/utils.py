def load_model(model_path):
    import joblib
    return joblib.load(model_path)

def preprocess_image(image):
    import cv2
    # Resize image to the required input size for the model
    image = cv2.resize(image, (224, 224))  # Example size, adjust as needed
    # Normalize the image
    image = image / 255.0
    return image

def save_output(output_path, results):
    import json
    with open(output_path, 'w') as f:
        json.dump(results, f)

def load_images_from_folder(folder):
    import os
    images = []
    for filename in os.listdir(folder):
        img_path = os.path.join(folder, filename)
        if os.path.isfile(img_path):
            images.append(img_path)
    return images

def load_video_frames(video_path):
    import cv2
    frames = []
    cap = cv2.VideoCapture(video_path)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    cap.release()
    return frames