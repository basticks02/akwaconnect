import requests
from bs4 import BeautifulSoup
import json

url = "https://forebears.io/nigeria/akwa-ibom/surnames"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extract surnames from the table
    names = [a.text.strip() for a in soup.select("table tbody tr td:nth-child(2) a")]

    # Save the names to a JSON file
    with open("akwa_ibom_names.json", "w", encoding="utf-8") as f:
        json.dump(names, f, ensure_ascii=False, indent=4)

    print(f"Saved {len(names)} Akwa Ibom names to akwa_ibom_names.json")
else:
    print(f"Error: Unable to fetch data, status code {response.status_code}")
