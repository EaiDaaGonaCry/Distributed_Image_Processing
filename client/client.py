from importlib.metadata import files

import requests
import sys
import os

def send_image(input_path: str, filter_type: str, output_path: str):
    url = "http://127.0.0.1:8000/process"

    if not os.path.exists(input_path):
        print(f"Error: Input file '{input_path}' not found.")
        return

    print(f"Sending {input_path} to server with filter '{filter_type}'...")

    with open(input_path, 'rb') as img_file:
        files_ = {'file': img_file}
        data_ = {'filter_type': filter_type}

        try:
            response = requests.post(url, files = files_, data = data_)
            response.raise_for_status()

            with open(output_path,'wb') as out_file:
                out_file.write(response.content)

            print(f"Success! Processed image saved to {output_path}")

        except requests.exceptions.RequestException as e:
            print(f"Network error or server failure: {e}")
            if response is not None:
                print(f"Server message: {response.text}")
