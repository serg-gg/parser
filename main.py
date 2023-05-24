import nofluffjobs
from mysql.connector import connect, Error
import getpass


def db_connect(vacancies):
    insert_vacancies_query = """
        INSERT INTO Vacancies
        (position, link)
        VALUES ( %s, %s )
        """
    select_vacancies_query = "SELECT * FROM Vacancies"
    try:
        with connect(
            host="localhost",
            user=input('User: '),
            password=getpass.getpass('Password: '),
            database="VacanciesDB",
        ) as connection:
            with connection.cursor() as cursor:
                cursor.executemany(insert_vacancies_query, vacancies)
                connection.commit()
                cursor.execute(select_vacancies_query)
                result = cursor.fetchall()
                for row in result:
                    print(row)

    except Error as e:
        print(e)


if __name__ == "__main__":
    db_connect(nofluffjobs.get_vacancies_links(nofluffjobs.get_vacancies_soup(nofluffjobs.pages, nofluffjobs.URL)))
