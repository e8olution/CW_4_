class Vacancy:
    def __init__(self, title, link, salary, description, requirements):
        self.title = title
        self.link = link
        self.salary = salary
        self.description = description
        self.requirements = requirements

    def __str__(self):
        return (f'Title: {self.title}\nLink: '
                f'{self.link}\nSalary: {self.salary}\n'
                f'Description: {self.description}\nRequirements: {self.requirements}\n')

    @staticmethod
    def _parse_salary(salary):
        if not salary:
            return "Зарплата не указана"
        if isinstance(salary, dict):
            salary_from = salary.get("from")
            salary_to = salary.get("to")
            currency = salary.get("currency", "руб.")
            if salary_from and salary_to:
                return f"{salary_from}-{salary_to} {currency}"
            if salary_from:
                return f"от {salary_from} {currency}"
            if salary_to:
                return f"до {salary_to} {currency}"
        return "Зарплата не указана"

    def get_salary_min(self):
        if isinstance(self.salary, str) and self.salary != "Зарплата не указана":
            # Удаляем пробелы и лишние символы
            salary_min_str = (self.salary.split('-')[0].replace("от ", "")
                              .replace("руб.", "").replace("RUR", "")
                              .replace("UZS", "").strip())
            # Преобразуем в int, если строка не пустая
            return int(salary_min_str) if salary_min_str.isdigit() else 0
        return 0

    def __lt__(self, other):
        return self.get_salary_min() < other.get_salary_min()
