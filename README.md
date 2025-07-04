# Prompt_wars
## OBSCURA 🕵️‍♀️ — AI-Powered Reality Distortion Detection System
Built by Team It’s Giving Jedi
AI for Good – Trust & Safety Track

## 🌐 Overview
In the age of AI-generated misinformation, distinguishing truth from manipulation is harder than ever. Whether it's a deepfake video, a viral meme, or a politically biased post — digital content is no longer what it seems.

OBSCURA is a cutting-edge AI platform designed to analyze and expose visual misinformation, with a focus on deepfake detection, emotional manipulation, and psychological framing.

Upload an image or video — OBSCURA does the rest.

## 🎯 What It Does
🔍 Detects deepfake images and videos

🧠 Analyzes cognitive manipulation techniques

🔥 Measures emotional intensity & bias

📊 Summarizes distortion levels with AI-generated insights and countermeasures

🧪 Deepfake Detection (Image & Video)
This core module of OBSCURA focuses on spotting synthetic media using ML models trained to detect:

Facial inconsistencies

Lighting anomalies

Compression artifacts

Frame-by-frame manipulation in videos

## 📁 Project Structure
bash
Copy
Edit
deepfake-detector/
│
├── src/
│   ├── image_detector.py      # Image deepfake detection logic
│   ├── video_detector.py      # Video deepfake detection logic
│   └── utils.py               # Shared helper functions
│
├── requirements.txt           # Required Python packages
├── README.md                  # You're reading it :)
└── .devcontainer/
    └── devcontainer.json      # Dev container config (optional)
## ⚙️ Installation
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/deepfake-detector.git
cd deepfake-detector
2. Create Virtual Environment (Recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
## 🧪 Usage
🔍 Image Deepfake Detection
python
Copy
Edit
from src.image_detector import detect_deepfake

result = detect_deepfake('path/to/image.jpg')
print('Is deepfake:', result)
## 🎥 Video Deepfake Detection
python
Copy
Edit
from src.video_detector import detect_deepfake_in_video

result = detect_deepfake_in_video('path/to/video.mp4')
print('Is deepfake:', result)
## 💼 Business Model
We’ve designed OBSCURA as a freemium platform:

Tier	Features
Free	Single-image detection, basic distortion metrics
Pro	Batch uploads, deeper psychological analysis, browser plugin (coming)
Enterprise	Bulk analysis tools, real-time scanning, API integration for platforms

We believe media literacy and truth access should be universal — not paywalled.

## 🔧 Tech Stack
Backend & AI
Python 🐍

PyTorch 🔬

NumPy 📊

CUDA ⚡

Three.js

webGL

Frontend
HTML / CSS / JavaScript

GSAP 🎞️

CSS Transforms

## 🛤 Roadmap
✅ MVP: Deepfake Detection (Image + Video)

🚀 Real-time browser extension (coming soon)

🧠 Advanced NLP + CV for emotional and logical distortion detection

🧩 API & dashboard for journalists, educators, and watchdogs

## 🤝 Contributing
We welcome contributions of all kinds!
Open an issue or submit a pull request for improvements, bug fixes, or feature requests.

## 📜 License
This project is licensed under the MIT License — because we believe open access to truth-detection tools is essential.

Challenges/bounties done:
1.dark theme
2.easter egg--light saber (loading page)
3.recreated popular scenes 
4.3d model -in homepage and also in deepfake scanner 

## 🙌 Acknowledgments
Inspired by real-world challenges in digital trust & safety

Built for the AI for Good – Media Integrity & Digital Awareness track

Designed with collaboration, transparency, and ethics at its core

"We don't just fight fake news — we expose the subtle, psychological distortion hiding in everyday content."
— Team It’s Giving Jedi

