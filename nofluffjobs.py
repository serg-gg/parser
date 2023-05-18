import main

nofluffjobs_request = main.get_request('https://nofluffjobs.com/pl/praca-zdalna?criteria=city%3Dwarszawa%20seniority%3Dtrainee&page=1')
nofluffjobs_soup = main.get_soup(nofluffjobs_request.content)


paginator = nofluffjobs_soup.find('div', {'class': 'text-center mt-5 ng-star-inserted'})
pages = paginator.find_all('a')
for index in range(len(pages)-1):
    print(f'page={(index+1)}')