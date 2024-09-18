class Vacancy:
    __slots__ = ["title", "url", "salary", "requirements"]

    def __init__(self, title: str, url: str, salary: str, requirements: str):
        self.title = self.__validate_title(title)
        self.url = url
        self.salary = salary
        self.requirements = requirements

    @staticmethod
    def __validate_title(title: str) -> str:
        if not title:
            raise ValueError("Название вакансии не может быть пустым")
        return title

    def __lt__(self, other: "Vacancy") -> bool:
        return self.get_salary_min() < other.get_salary_min()

    def __gt__(self, other: "Vacancy") -> bool:
        return self.get_salary_min() > other.get_salary_min()

    def get_salary_min(self) -> int:
        # Проверяем, что поле зарплаты не является строкой "Не указана" или None
        if isinstance(self.salary, dict):
            # Если salary - это словарь, пытаемся взять минимальную зарплату
            return self.salary.get("from", 0) or 0
        elif isinstance(self.salary, str) and '-' in self.salary:
            # Если salary - это строка с диапазоном зарплаты
            return int(self.salary.split('-')[0].replace(' ', '').replace('руб.', ''))
        else:
            # Если формат зарплаты неизвестен или она не указана
            return 0

    @classmethod
    def cast_to_object_list(cls, vacancies: list) -> list:
        return [
            cls(
                v["name"],
                v["alternate_url"],
                v.get("salary", {"from": 0, "to": 0}),  # Предполагаем, что salary может быть словарём или строкой
                v["snippet"].get("requirement", "Требования не указаны")  # Требования могут быть не указаны
            )
            for v in vacancies if v.get("snippet")
        ]
