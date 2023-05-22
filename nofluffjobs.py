import main

URL = 'https://nofluffjobs.com/pl/praca-zdalna?criteria=city%3Dwarszawa%20seniority%3Dtrainee&page=1'

nofluffjobs_request = main.get_request(URL)
nofluffjobs_soup = main.get_soup(nofluffjobs_request.content)


paginator = nofluffjobs_soup.find('div', {'class': 'text-center mt-5 ng-star-inserted'})
pages = paginator.find_all('a')

main.get_vacancies_links(main.get_vacancies_soup(pages, URL))