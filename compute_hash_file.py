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
        
# file_path = 'original.png'
# print("Python hash:", compute_hash(file_path))