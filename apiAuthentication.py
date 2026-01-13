import os

import requests
from dotenv import load_dotenv

load_dotenv()
url = "https://api.github.com/user"
API_KEY = os.getenv("USER_KEY")

headers = {
    'Authorization': f'Bearer {API_KEY}'
}

print(requests.get(url, headers=headers).json())