# Reading from a file
with open("sample.txt", "r") as file:
    content = file.read()
    print("File Content:")
    print(content)

# Writing to a file
with open("output.txt", "w") as file:
    file.write("Hello, this is written to a file.")
3. Web Scraping with BeautifulSoup:
python
Copy code
import requests
from bs4 import BeautifulSoup

url = "https://www.example.com"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.title.string
    print(f"Title of the website: {title}")
else:
    print(f"Error accessing {url}. 
