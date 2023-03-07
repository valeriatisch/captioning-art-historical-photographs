"""
The Artpedia JSON file contains a list of visual sentences for each image.
This script creates one entry per each visual sentence.
We use this annotation later for finetuning to have more samples per image.
"""

import argparse
import json

# Set up argparse to allow input and output file paths to be specified via command line arguments
parser = argparse.ArgumentParser(description='Formatting Artpedia JSON file')
parser.add_argument('input_file', help='Path to the input JSON file')
parser.add_argument('output_file', help='Path to the output JSON file')
args = parser.parse_args()

# Read the input JSON file
with open(args.input_file) as json_file:
    annotations = json.load(json_file)

new_annotations = []
counter = 0

# Loop through each image in the input JSON file
for idx, sample in enumerate(annotations):
    # Loop through each caption for the current image
    for caption in sample["caption"]:
        # Create a new dictionary with the caption, and image data
        new_sample = {
            "image_id": idx,
            "id": counter,
            "caption": caption,
            "image": sample["image"]
        }
        new_annotations.append(new_sample)
        counter += 1

# Write the new annotations to the output file
with open(args.output_file, "w") as f:
    json.dump(new_annotations, f, indent=4)
