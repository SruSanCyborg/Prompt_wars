import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ImageDetector:
    def __init__(self, model_path=None):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        logger.info(f"Using device: {self.device}")
        
        self.model = self._load_model(model_path)
        self.model.eval()
        
        self.transform = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])
        
        self.fake_threshold = 0.6  # Adjust based on your model's performance
        
    def _load_model(self, model_path):
        """Load model with proper binary classification setup"""
        logger.info("Initializing ResNet18 with binary classification")
        
        # Load base model
        model = models.resnet18(pretrained=False)  # Start with untrained
        
        # Modify for binary classification
        num_features = model.fc.in_features
        model.fc = nn.Sequential(
            nn.Linear(num_features, 512),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(512, 2)  # [real, fake]
        )
        
        # Load trained weights if available
        if model_path and os.path.exists(model_path):
            try:
                logger.info(f"Loading weights from {model_path}")
                model.load_state_dict(torch.load(model_path, map_location=self.device))
                logger.info("Weights loaded successfully")
            except Exception as e:
                logger.error(f"Error loading weights: {str(e)}")
                # Continue with untrained weights if loading fails
        
        return model.to(self.device)
        
    def predict(self, image_path):
        """Make prediction on an image file"""
        try:
            # Load and verify image
            img = Image.open(image_path)
            if img.mode != 'RGB':
                img = img.convert('RGB')
                
            # Preprocess
            img_tensor = self.transform(img).unsqueeze(0).to(self.device)
            
            # Predict
            with torch.no_grad():
                outputs = self.model(img_tensor)
                probabilities = torch.softmax(outputs, dim=1)
                fake_prob = probabilities[0][1].item()  # Probability of being fake
                
            print("Fake probability:", fake_prob)
            print("Prediction:", 'fake' if fake_prob > self.fake_threshold else 'real')
                
            return {
                'prediction': 'fake' if fake_prob > self.fake_threshold else 'real',
                'confidence': max(fake_prob, 1 - fake_prob),
                'is_fake': fake_prob > self.fake_threshold,
                'raw_probability': fake_prob
            }
            
        except Exception as e:
            logger.error(f"Prediction failed: {str(e)}")
            return {
                'error': str(e),
                'prediction': 'error',
                'confidence': 0.0
            }