import nofluffjobs


if __name__ == "__main__":
    print(nofluffjobs.get_vacancies_links(nofluffjobs.get_vacancies_soup(nofluffjobs.pages, nofluffjobs.URL)))