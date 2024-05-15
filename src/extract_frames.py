import cv2
import os

def extract_frames(video_path, output_folder, interval=30):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    vidcap = cv2.VideoCapture(video_path)
    success, image = vidcap.read()
    count = 0

    while success:
        if count % interval == 0:
            frame_path = os.path.join(output_folder, f"frame_{count:03d}.jpg")
            cv2.imwrite(frame_path, image)
        success, image = vidcap.read()
        count += 1

    vidcap.release()

if __name__ == "__main__":
    extract_frames('data/raw_videos/sample_video.mp4', 'data/frames')
