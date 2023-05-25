import nofluffjobs
from mysql.connector import connect, Error
import telebot, os


def db_connect(vacancies):
    new_vacancies = []
    select_vacancies_query = "SELECT Position, Link FROM Vacancies"
    try:
        with connect(
            host="localhost",
            user=os.getenv('MYSQL_USER'),
            password=os.getenv('MYSQL_PASSWORD'),
            database="VacanciesDB",
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(select_vacancies_query)
                vacancies_in_db = cursor.fetchall()
                for v in vacancies:
                    if v not in vacancies_in_db:
                        new_vacancies.append(v)
                        insert_vacancies_query = f"INSERT INTO Vacancies (position, link) VALUES {v}"
                        cursor.execute(insert_vacancies_query)
                connection.commit()
        return new_vacancies

    except Error as e:
        print(e)


with open('C:\\Users\\s_bur\\PycharmProjects\\parser\\my_token') as file:
    BOT_TOKEN = file.read()

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def send_vacancies(message):
    for v in db_connect(nofluffjobs.get_vacancies_links(nofluffjobs.get_vacancies_soup(nofluffjobs.pages, nofluffjobs.URL))):
        bot.send_message(message.chat.id, v[0], v[1])


if __name__ == "__main__":
    bot.infinity_polling()