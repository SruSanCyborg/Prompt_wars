# PROMPT_WARS
## OBSCURA 🕵️‍♀️ — AI-Powered Reality Distortion Detection System
Built by Team It’s Giving Jedi
AI for Good – Trust & Safety Track

Track -Fullstackdevelopment 

## 🌐 Overview
In the age of AI-generated misinformation, distinguishing truth from manipulation is harder than ever. Whether it's a deepfake video, a viral meme, or a politically biased post — digital content is no longer what it seems.

OBSCURA is a cutting-edge AI platform designed to analyze and expose visual misinformation, with a focus on deepfake detection, emotional manipulation, and psychological framing.

Upload an image or video — OBSCURA does the rest.

Problem Statement:
In today’s digital world, we’re constantly exposed to content designed to manipulate us — not inform us.
From AI-generated articles and deepfake videos to emotionally charged tweets and biased headlines, reality is being distorted in subtle, powerful ways.
This manipulation isn’t always obvious — it uses guilt, fear, emotional framing, and confirmation bias to shape how we think and feel.
As a result, people are unknowingly trapped in digital echo chambers that reinforce beliefs instead of challenging them.
We’re not just dealing with misinformation — we’re dealing with psychological influence at scale.
Fact-checkers and moderation tools focus on what’s false, but they don’t show users how they’re being influenced.
There’s no accessible, interactive platform that breaks down the hidden emotional and cognitive tactics used in everyday content.
This leads to a growing crisis of trust, confusion, and manipulation — especially for those without technical expertise.
People need more than truth — they need clarity, awareness, and defense against manipulation.
Obscura is our solution: an AI-powered system that reveals the hidden layers of distortion in text, media, and video — and helps users see with open eyes.

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

Challenges/bounties done:
1.dark theme
2.easter egg--light saber (loading page)
3.recreated popular scenes 
4.3d model -in homepage and also in deepfake scanner 

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
🧪 Usage
🔍 Image Deepfake Detection
python
Copy
Edit
from src.image_detector import detect_deepfake

result = detect_deepfake('path/to/image.jpg')
print('Is deepfake:', result)
🎥 Video Deepfake Detection
python
Copy
Edit
from src.video_detector import detect_deepfake_in_video

result = detect_deepfake_in_video('path/to/video.mp4')
print('Is deepfake:', result)
💼 Business Model
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
Three.JS
CUDA ⚡

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

💼 Obscura Business Model
🔹 1. Freemium Tier (For Individuals)
✅ Target Users: Students, curious individuals, casual users
✅ Features:

Limited daily scans of text/images

Basic TruthLens analysis (manipulation score, emotional bias, etc.)

Access to community scan history and education section

✅ Purpose: Raise awareness, build user trust, gather feedback

## 🙌 Acknowledgments
Inspired by real-world challenges in digital trust & safety

Built for the AI for Good – Media Integrity & Digital Awareness track

Designed with collaboration, transparency, and ethics at its core

"We don't just fight fake news — we expose the subtle, psychological distortion hiding in everyday content."
— Team It’s Giving Jedi
