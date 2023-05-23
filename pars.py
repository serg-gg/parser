import requests
from bs4 import BeautifulSoup


class Parser:

    def get_request(url):
        return requests.get(url)

    def get_soup(content):
        return BeautifulSoup(content, 'html.parser')


