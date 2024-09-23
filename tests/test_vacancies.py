import unittest
from src.vacancies import Vacancy


class TestVacancy(unittest.TestCase):

    def setUp(self):
        self.vacancy = Vacancy(
            title="Менеджер по туризму",
            link="https://hh.ru/vacancy/123456",
            salary={"from": 50000, "to": 100000, "currency": "RUR"},
            description="Работа с клиентами, продажа туров.",
            requirements="Опыт работы не менее 1 года."
        )

    def test_str_representation(self):
        expected_str = ("Title: Менеджер по туризму\nLink: "
                        "https://hh.ru/vacancy/123456\nSalary: {'from': 50000, 'to': 100000, 'currency': 'RUR'}\n"
                        "Description: Работа с клиентами, продажа туров.\nRequirements: Опыт работы не менее 1 года.\n")
        self.assertEqual(str(self.vacancy), expected_str)

    def test_parse_salary(self):
        self.assertEqual(self.vacancy._parse_salary(self.vacancy.salary), "50000-100000 RUR")
        self.assertEqual(self.vacancy._parse_salary(None), "Зарплата не указана")
        self.assertEqual(self.vacancy._parse_salary({"from": 30000}), "от 30000 RUR")
        self.assertEqual(self.vacancy._parse_salary({"to": 70000}), "до 70000 RUR")

    def test_get_salary_min(self):
        self.assertEqual(self.vacancy.get_salary_min(), 50000)

        # Тест с пустой зарплатой
        vacancy_no_salary = Vacancy("Без зарплаты", "link", None, "Описание", "Требования")
        self.assertEqual(vacancy_no_salary.get_salary_min(), 0)

    def test_comparison_operator(self):
        vacancy_high_salary = Vacancy(
            title="Генеральный директор",
            link="https://hh.ru/vacancy/654321",
            salary={"from": 200000, "to": 300000, "currency": "RUR"},
            description="Руководство компанией.",
            requirements="Опыт работы от 5 лет."
        )
        self.assertTrue(vacancy_high_salary > self.vacancy)


if __name__ == '__main__':
    unittest.main()
