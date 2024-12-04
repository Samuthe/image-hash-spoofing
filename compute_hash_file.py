#!/usr/bin/env python3

import hashlib
import random
import os
from PIL import Image, PngImagePlugin, JpegImagePlugin

#function to compute hash of an image
def compute_hash(file_path, algorithm='sha512'):
    """Compute hash of an image(sha256sum) using a given algorithm.
    """
    with open(file_path, 'rb') as f:
        file_data = f.read() # Read the entire file as a single byte string
        # Compute hash
        if algorithm == 'sha512':
            return hashlib.sha512(file_data).hexdigest()
# Test the function  
# file_path = 'original.png'
# print("Python hash:", compute_hash(file_path))


# Function to append random data to an image file
def append_random_data(file_path, output_path, length=16):
    """
    Appends random bytes to the end of the file.
    """
    with open(file_path, "rb") as original_file:
        file_data = original_file.read()  # Read original file data
    with open(output_path, "wb") as modified_file:
        modified_file.write(file_data)  # Write the original data
        # Append random bytes
        modified_file.write(os.urandom(length))
        
# Test the function
# file_path = 'original.png'
# output_path = 'modified.png'
# append_random_data(file_path, output_path, length=16)
# print(f"Random data appended to the file: {output_path}")


def spoof_image(prefix, input_image, output_image, max_attempts=1000):
    """
    Spoof an image by appending random bytes to the end of the file.
    """
    attempt = 0
    while attempt < max_attempts:
        attempt += 1
        # Append random data to the image
        append_random_data(input_image, output_image, length=16)
        # Compute hash of the modified image
        modified_hash = compute_hash(output_image)
        # Check if the hash starts with the given prefix
        if modified_hash.startswith(prefix):
            print(f"Image spoofed successfully in {attempt} attempts.")
            return
        if attempt % 100 == 0:
            print(f"Attempt {attempt}, current hash: {modified_hash[:len(prefix)]}")
    print("Failed to spoof image within max attempts.")
    
# Test the function
# spoof_image('99', 'original.png', 'spoofed.png')

