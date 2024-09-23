def filter_vacancies(vacancies, search_query):
    search_query_lower = search_query.lower()

    filtered_vacancies = []
    for vacancy in vacancies:
        description = vacancy.description if vacancy.description else ""
        description_contains_query = search_query_lower in description.lower()

        if description_contains_query:
            filtered_vacancies.append(vacancy)

    return filtered_vacancies


def sort_vacancies(vacancies):
    return sorted(vacancies, reverse=True, key=lambda vac: vac.get_salary_min())


def get_top_vacancies(vacancies, top_n):
    return vacancies[:top_n]
