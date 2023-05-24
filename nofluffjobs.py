from pars import Parser

URL = 'https://nofluffjobs.com/pl/praca-zdalna/Python?criteria=city%3Dwarszawa%20%20seniority%3Dtrainee,junior&page=1'

nofluffjobs_request = Parser.get_request(URL)
nofluffjobs_soup = Parser.get_soup(nofluffjobs_request.content)
nofluffjobs_paginator = nofluffjobs_soup.find('div', {'class': 'text-center mt-5 ng-star-inserted'})
if nofluffjobs_paginator:
    pages = nofluffjobs_paginator.find_all('a')
else:
    pages = nofluffjobs_soup


def get_vacancies_soup(pages, url):
    if nofluffjobs_paginator:
        for page_index in range(len(pages) - 1):
            current_page = Parser.get_request(f'{url}&page={(page_index + 1)}')
            soup = Parser.get_soup(current_page.content)
            vacancies_soup = soup.find('div', {'class': 'list-container ng-star-inserted'})
    else:
        vacancies_soup = pages.find('div', {'class': 'list-container ng-star-inserted'})
    return vacancies_soup


def get_vacancies_links(vacancies_soup):
    vacancies = []
    for v in vacancies_soup:
        v = str(v).split('\n')
        for st in v:
            if st.startswith('<a') and 'href=' in st:
                title = st[(st.index('listing">')+10):(st.index('</h3')-1)]
                start_index = st.index('href') + 6
                end_index = st[start_index:].index('"') + start_index
                link = 'https://nofluffjobs.com' + st[start_index:end_index]
                vacancies.append((title, link))
    return vacancies

