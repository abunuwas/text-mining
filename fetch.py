import requests
from bs4 import BeautifulSoup as bs

def fetch(url, output):
	content = requests.get(url).content
	text = bs(content, 'html.parser').text
	with open(output, 'w', encoding='utf-8') as file:
		file.write(text)
	return None


response = fetch('http://lib.ru/FOUNDATION/nightfall.txt', 'asimov.txt')
print(response)