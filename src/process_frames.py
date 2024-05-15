import torch
from PIL import Image
import clip
import os

def process_frames(frames_folder, output_folder):
    model, preprocess = clip.load("ViT-B/32")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for frame_name in os.listdir(frames_folder):
        frame_path = os.path.join(frames_folder, frame_name)
        image = Image.open(frame_path)
        image_input = preprocess(image).unsqueeze(0)

        with torch.no_grad():
            image_features = model.encode_image(image_input)

        features_path = os.path.join(output_folder, f"{os.path.splitext(frame_name)[0]}_features.pt")
        torch.save(image_features, features_path)

if __name__ == "__main__":
    process_frames('data/frames', 'data/processed_features')
