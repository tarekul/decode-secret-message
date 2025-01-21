import re
import requests
from bs4 import BeautifulSoup

def decodeSecretMessage(url):
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
    else:
        print(f"Failed to fetch the document. Status code: {response.status_code}")
        exit()

    soup = BeautifulSoup(html_content, 'html.parser')
    
    table = soup.find('table')
    rows = table.find_all('tr')
    data = []
    
    for row in rows[1:]:
        cols = row.find_all('td')
        if len(cols) == 3:
            x = int(cols[0].text.strip())
            char = cols[1].text.strip()
            y = int(cols[2].text.strip())
            data.append((x, y, char))
    
    if not data:
        print("No data found in the document.")
        return
    
    max_x = max(x for x, _, _ in data)
    max_y = max(y for _, y, _ in data)
    
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    
    for x, y, char in data:
        grid[y][x] = char
        
    for row in reversed(grid):
        print(''.join(row))    

url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
decodeSecretMessage(url)