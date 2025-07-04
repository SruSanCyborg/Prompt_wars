# Deepfake Detector

This project implements a deepfake detection system for both images and videos. It utilizes machine learning algorithms to identify manipulated content, providing tools for researchers and developers to analyze and detect deepfakes effectively.

## Project Structure

- `src/`
  - `image_detector.py`: Contains the implementation of the image deepfake detection algorithm.
  - `video_detector.py`: Implements the video deepfake detection functionality.
  - `utils.py`: Includes utility functions used across the image and video detection modules.
  
- `requirements.txt`: Lists the required Python libraries for the project.

- `README.md`: Documentation for the project.

- `.devcontainer/`
  - `devcontainer.json`: Configuration for the development container.

## Installation

To set up the environment, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/deepfake-detector.git
   cd deepfake-detector
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Image Detection

To detect deepfakes in images, use the `image_detector.py` script. You can load an image and apply the detection model as follows:

```python
from src.image_detector import detect_deepfake

result = detect_deepfake('path/to/image.jpg')
print('Is deepfake:', result)
```

### Video Detection

For video deepfake detection, use the `video_detector.py` script. It processes each frame of the video:

```python
from src.video_detector import detect_deepfake_in_video

result = detect_deepfake_in_video('path/to/video.mp4')
print('Is deepfake:', result)
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.