import torch
import torchvision.transforms as transforms
from PIL import Image
import timm


class DepthEstimation:
    def __init__(self, model_name='MiDaS'):
        if model_name == 'MiDaS':
            self.model = torch.hub.load("intel-isl/MiDaS", "MiDaS")
        elif model_name == 'DPT':
            self.model = timm.create_model('dpt_small', pretrained=True)
        else:
            raise ValueError(f"Unsupported model name: {model_name}")

        self.model.eval()
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model.to(self.device)

    def preprocess_image(self, image_path):
        transform = transforms.Compose([
            transforms.Resize((384, 384)),  # MiDaS model requires input image size to be multiple of 32
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])
        image = Image.open(image_path).convert("RGB")
        image = transform(image).unsqueeze(0).to(self.device)
        return image

    def predict_depth(self, image_path):
        input_image = self.preprocess_image(image_path)
        with torch.no_grad():
            prediction = self.model(input_image)
        depth_map = prediction.squeeze().cpu().numpy()
        return depth_map
