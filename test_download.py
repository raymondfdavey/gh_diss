import os
import ssl
import certifi
from urllib.request import urlopen

os.environ['SSL_CERT_FILE'] = certifi.where()

url = "https://zenodo.org/record/2540695/files/0.model?download=1"

try:
    with urlopen(url) as response:
        print("Connection successful!")
        data = response.read()
        print(f"Downloaded {len(data)} bytes")
except Exception as e:
    print(f"An error occurred: {e}")