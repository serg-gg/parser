import requests
from bs4 import BeautifulSoup


def get_request(url):
    return requests.get(url)


def get_soup(content):
    return BeautifulSoup(content, 'html.parser')


def get_vacancies_soup(pages, url):
    for page_index in range(len(pages) - 1):
        current_page = requests.get(f'{url}&page={(page_index + 1)}')
        soup = get_soup(current_page.content)
        vacancies_soup = soup.find('div', {'class': 'list-container ng-star-inserted'})
    return vacancies_soup


def get_vacancies_links(vacancies_soup):
    vacancies = []
    for v in vacancies_soup:
        v = str(v).split('\n')
        for st in v:
            if st.startswith('<a') and 'href=' in st:
                start_index = st.index('href') + 6
                end_index = st[start_index:].index('"') + start_index
                link = 'https://nofluffjobs.com' + st[start_index:end_index]
                vacancies.append(link)
    return vacancies