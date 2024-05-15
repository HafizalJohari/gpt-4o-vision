import clip
import torch
from PIL import Image

class VisionModel:
    def __init__(self, model_name="ViT-B/32"):
        self.model, self.preprocess = clip.load(model_name)
    
    def extract_features(self, image_path):
        image = Image.open(image_path)
        image_input = self.preprocess(image).unsqueeze(0)

        with torch.no_grad():
            image_features = self.model.encode_image(image_input)
        
        return image_features
