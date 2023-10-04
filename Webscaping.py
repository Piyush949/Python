import requests
from bs4 import BeautifulSoup

url = "https://www.example.com"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.title.string
    print(f"Title of the website: {title}")
else:
    print(f"Error accessing {url}. Status code: {response.status_code}")
