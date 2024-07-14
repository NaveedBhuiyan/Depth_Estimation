# Depth Estimation with PyTorch

This project demonstrates depth estimation using pretrained models in PyTorch, specifically the MiDaS and DPT models. It provides a modular approach using object-oriented programming for model loading, image preprocessing, depth prediction, and visualization.

## Installation and Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/depth-estimation.git
   cd depth-estimation

2. Install dependencies
    
    ```bash
    pip install -r requirements.txt

3. Usage

    1. Place your input image(s) in the sample_image directory.

    2. Modify main.py to specify the input image path (image_path variable).

    3. Run the script to perform depth estimation and save the output depth map:

    ```bash
    python main.py

By default, the depth map will be saved as output_depth_map.jpeg in the project directory.

## Project structure

1. main.py: Main script to demonstrate depth estimation using the DepthEstimation and Visualizer classes.
2. depth_estimation.py: Contains the DepthEstimation class for loading models, preprocessing images, and predicting depth.
3. visualizer.py: Contains the Visualizer class with a static method for visualizing and saving depth maps.
4. sample_image/: Directory for storing sample input images

# License
This project is licensed under the MIT License

# Acknowledgments
The MiDaS model from intel-isl/MiDaS and DPT models from timm library.
PyTorch community and contributors.