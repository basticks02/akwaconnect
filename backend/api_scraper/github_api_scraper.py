import os
import requests
from dotenv import load_dotenv

load_dotenv()
GITHUB_API_KEY = os.getenv("GITHUB_API_KEY")

API_URL = "https://api.github.com/search/users?q=software+engineer"

HEADERS = {"Authorization": f"token {GITHUB_API_KEY}"}

def fetch_github_users():
    response = requests.get(API_URL, headers=HEADERS)

    if response.status_code == 200:
        users = response.json().get("items", [])
        for user in users:
            print(user["login"], "-", user["html_url"])
    else:
        print("Error:", response.status_code, response.text)

if __name__ == "__main__":
    fetch_github_users()
