# pip install requests
# pip install beautifulsoup4
import requests
from bs4 import BeautifulSoup

url = "https://www.bu.edu/president/boston-university-facts-stats/"
response = requests.get(url)

status = response.status_code

content = response.content
soup = BeautifulSoup(content, "html.parser")
print(soup.title)
print(soup.title.get_text())
# print(soup.body)
print(response.status_code)


