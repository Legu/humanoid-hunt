from html.parser import HTMLParser
import http.client

from level1 import solve as level1
from level2 import solve as level2
from level3 import solve as level3

CHALLENGES = {
	'/tattoo': level1,
	'/nanobots': level2,
	'/android': level3,
}

class MyHTMLParser(HTMLParser):
	def __init__(self):
		self.capturing = False
		self.data = ''
		super().__init__()

	def handle_starttag(self, tag, attrs):
		if tag == 'code' and ('id', 'puzzle-data') in attrs:
			self.capturing = True

	def handle_endtag(self, tag):
		if tag == 'code':
			self.capturing = False

	def handle_data(self, data):
		if self.capturing:
			self.data += data

def get_challenge_data(conn, url):
	conn.request('GET', url)
	response = conn.getresponse()
	data = response.read().decode('utf-8')
	parser = MyHTMLParser()
	parser.feed(data)
	return parser.data

if __name__ == '__main__':
	conn = http.client.HTTPSConnection('hunt.reaktor.com')
	for url,func in CHALLENGES.items():
		data = get_challenge_data(conn, url)
		solution = func(data)
		print(url, solution)
