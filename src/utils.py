def filter_vacancies(vacancies: list, keywords: list) -> list:
    return [v for v in vacancies if any(keyword.lower() in v.title.lower() for keyword in keywords)]

def get_vacancies_by_salary(vacancies: list, salary_range: str) -> list:
    salary_min, salary_max = map(int, salary_range.split('-'))
    return [v for v in vacancies if salary_min <= v.get_salary_min() <= salary_max]

def sort_vacancies(vacancies: list) -> list:
    return sorted(vacancies, reverse=True)

def get_top_vacancies(vacancies: list, top_n: int) -> list:
    return vacancies[:top_n]

def print_vacancies(vacancies: list):
    for vacancy in vacancies:
        print(f"Вакансия: {vacancy.title}\nURL: {vacancy.url}\nЗарплата: {vacancy.salary}\n")
