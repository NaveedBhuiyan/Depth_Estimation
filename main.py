from src.depth_estimation import DepthEstimation
from src.visualizer import Visualizer

if __name__ == "__main__":
    image_path = 'sample_image/images.jpeg'

    # Initialize depth estimation
    depth_estimator = DepthEstimation(model_name='MiDaS')

    # Predict depth map
    depth_map = depth_estimator.predict_depth(image_path)

    # Visualize and save depth map
    save_path = 'output_depth_map.jpeg'
    Visualizer.visualize_depth_map(depth_map, save_path)
