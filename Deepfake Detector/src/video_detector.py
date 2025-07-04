import cv2
from image_detector import ImageDetector

class VideoDetector:
    def __init__(self, image_detector=None):
        # Accept an ImageDetector instance
        self.image_detector = image_detector or ImageDetector()

    def process_frame(self, frame):
        # Save frame temporarily to disk for compatibility with ImageDetector
        temp_path = 'temp_frame.jpg'
        cv2.imwrite(temp_path, cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
        result = self.image_detector.predict(temp_path)
        # Optionally, remove the temp file
        try:
            import os
            os.remove(temp_path)
        except Exception:
            pass
        # Interpret result: return True if 'fake' label has higher score
        if isinstance(result, list):
            for r in result:
                if r.get('label') == 'fake' and r.get('score', 0) > 0.5:
                    return True
        return False

    def detect_deepfake_in_video(self, video_path):
        cap = cv2.VideoCapture(video_path)
        deepfake_count = 0
        total_frames = 0

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            total_frames += 1
            if self.process_frame(frame):
                deepfake_count += 1

        cap.release()
        return deepfake_count / total_frames if total_frames > 0 else 0

# Example usage:
# image_detector = ImageDetector('path_to_model_directory')
# video_detector = VideoDetector(image_detector)
# result = video_detector.detect_deepfake_in_video('path_to_video.mp4')
# print(f'Deepfake probability: {result}')