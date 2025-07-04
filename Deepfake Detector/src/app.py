import os
import time
import traceback
from flask import Flask, render_template, request, redirect, url_for
from PIL import Image
import kagglehub
from image_detector import ImageDetector

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Initialize detector with Kaggle model
def initialize_detector():
    try:
        # Download the model from Kaggle Hub
        model_path = kagglehub.model_download("manjilkarki/deepfake-detection-model/resnet18/v1.0")
        print(f"Model downloaded to: {model_path}")
        
        # Initialize detector with the downloaded model
        return ImageDetector(model_path=os.path.join(model_path, "model.pth"))
    except Exception as e:
        print(f"Error loading Kaggle model: {str(e)}")
        # Fallback to untrained model if Kaggle fails
        return ImageDetector()

image_detector = initialize_detector()

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', result='No file selected')
            
        file = request.files['file']
        if file.filename == '':
            return render_template('index.html', result='No file selected')
            
        if file and allowed_file(file.filename):
            try:
                # Save uploaded file temporarily
                filename = file.filename
                save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
                file.save(save_path)
                
                # Verify image
                try:
                    with Image.open(save_path) as img:
                        img.verify()
                except Exception as e:
                    os.remove(save_path)
                    return render_template('index.html', result=f"Invalid image: {str(e)}")
                
                # Make prediction
                result = image_detector.predict(save_path)
                os.remove(save_path)  # Clean up
                
                if 'error' in result:
                    return render_template('index.html', result=f"Error: {result['error']}")
                
                return render_template('index.html', 
                                    result=f"Prediction: {result['prediction'].upper()} (Confidence: {result['confidence']:.2%})")
                
            except Exception as e:
                if os.path.exists(save_path):
                    os.remove(save_path)
                return render_template('index.html', result=f"Processing error: {str(e)}")
                
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)