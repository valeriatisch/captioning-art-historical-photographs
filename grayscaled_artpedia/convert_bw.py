import argparse

import concurrent.futures
from pathlib import Path

from torchvision import transforms
from PIL import Image

# Define the command line arguments
parser = argparse.ArgumentParser(description='Converts images in a directory to grayscale')
parser.add_argument('input_dir', type=str, help='path to the input directory')
parser.add_argument('output_dir', type=str, help='path to the output directory')
args = parser.parse_args()

# Define input and output paths
path = Path(args.input_dir)
output_path = Path(args.output_dir)

# Set a high threshold for the maximum image size to avoid errors
Image.MAX_IMAGE_PIXELS = None

# Define grayscale transformation
transform = transforms.Grayscale()

# Use multithreading to parallelize the image processing step
with concurrent.futures.ThreadPoolExecutor() as executor:
    for file in path.glob('*.*'):
        if file.suffix not in ['.jpg', '.jpeg', '.png']:
            continue
        if (output_path / file.name).exists():
            continue
        with Image.open(file) as img:
            img = transform(img)
            img.save(output_path / file.name)
