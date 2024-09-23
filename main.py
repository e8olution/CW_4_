from src.api import HH
from src.vacancies import Vacancy
from src.file_handler import JSONSaver
from src.utils import filter_vacancies, sort_vacancies, get_top_vacancies


def user_interaction():
    hh_api = HH()
    json_saver = JSONSaver()

    while True:
        search_query = input("Введите поисковый запрос для поиска вакансий: ")
        if search_query:
            break
        print("Запрос не может быть пустым. Пожалуйста, попробуйте еще раз.")

    while True:
        top_n_input = input("Введите количество вакансий для вывода в топ N: ")
        if top_n_input.isdigit():
            top_n = int(top_n_input)
            break
        print("Пожалуйста, введите корректное число.")

    filter_word = input("Введите ключевое слово для фильтрации вакансий по описанию (или оставьте пустым): ")

    hh_vacancies = hh_api.load_vacancies(search_query)

    if not hh_vacancies:
        print("Вакансии не найдены.")
        return

    # Создаем список объектов Vacancy
    vacancies_list = [
        Vacancy(
            item['name'],
            item['alternate_url'],
            item.get('salary', 'Зарплата не указана'),
            item['snippet'].get('responsibility', 'Описание не указано'),
            item['snippet'].get('requirement', 'Требования не указаны')
        )
        for item in hh_vacancies
    ]

    # Фильтруем вакансии по названию
    filtered_vacancies = filter_vacancies(vacancies_list, search_query)

    # Если указано ключевое слово, фильтруем по описанию
    if filter_word:
        filtered_vacancies = filter_vacancies(filtered_vacancies, filter_word)

    if not filtered_vacancies:
        print(f"Вакансии, содержащие ключевое слово '{filter_word}', не найдены.")
        return

    # Сортируем отфильтрованные вакансии по зарплате (или по другому критерию)
    sorted_vacancies = sort_vacancies(filtered_vacancies)

    # Выбираем топ N вакансий
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)

    # Сохранение вакансий в файл
    json_saver.save_vacancies_to_file(top_vacancies)

    print("Топ вакансий:")
    for vacancy in top_vacancies:
        print(f"Title: {vacancy.title}")
        print(f"Link: {vacancy.link}")
        print(f"Salary: {vacancy.salary}")
        print(f"Description: {vacancy.description}")
        print(f"Requirements: {vacancy.requirements}")
        print()

    print("Список вакансий добавлен и обновлен.")


if __name__ == "__main__":
    user_interaction()
