import requests
from bs4 import BeautifulSoup

# URL of the Wikipedia page
url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'

# Fetch the page
response = requests.get(url)
print(response.content)
soup = BeautifulSoup(response.content, 'html.parser')

# Find the content headings (these are inside <span class="mw-headline">)
p = soup.find_all('p')
pythonfile = 'python-content.txt'
print("📚 Wikipedia Headings on the Python page:\n")
def writeToFile(text):
    with open(pythonfile, 'a', encoding='utf-8') as f:
        f.write("\n"+text)
        
for i, el in enumerate(p, 1):
    print(el.text)
    writeToFile(el.text)

