import unittest
from src.vacancies import Vacancy
from src.utils import filter_vacancies, sort_vacancies, get_top_vacancies


class TestUtils(unittest.TestCase):

    def setUp(self):
        # Создаем несколько экземпляров Vacancy для тестов
        self.vacancies = [
            Vacancy(title="Менеджер", link="https://example.com/1", salary={"from": 50000},
                    description="Опыт работы с клиентами", requirements="Коммуникабельность, ответственность"),
            Vacancy(title="Программист", link="https://example.com/2", salary={"from": 80000},
                    description="Знания Python и Django", requirements="Опыт работы с Python и Django"),
            Vacancy(title="Курьер", link="https://example.com/3", salary={"from": 30000},
                    description=None, requirements="Физическая выносливость"),
            Vacancy(title="Менеджер по туризму", link="https://example.com/4", salary={"from": 60000},
                    description="Опыт работы в туризме", requirements="Знание туристических направлений"),
        ]

    def test_filter_vacancies(self):
        result = filter_vacancies(self.vacancies, "менеджер")
        self.assertEqual(len(result), 2)  # Должны вернуть 2 вакансии
        self.assertIn(self.vacancies[0], result)
        self.assertIn(self.vacancies[3], result)

        result = filter_vacancies(self.vacancies, "Python")
        self.assertEqual(len(result), 1)  # Должны вернуть 1 вакансию
        self.assertIn(self.vacancies[1], result)

        result = filter_vacancies(self.vacancies, "тестирование")
        self.assertEqual(len(result), 0)  # Не должно быть вакансий

    def test_sort_vacancies(self):
        sorted_vacancies = sort_vacancies(self.vacancies)
        self.assertEqual(sorted_vacancies[0].title, "Программист")  # Программист с самой высокой зарплатой

    def test_get_top_vacancies(self):
        top_vacancies = get_top_vacancies(self.vacancies, 2)
        self.assertEqual(len(top_vacancies), 2)  # Должны вернуть 2 вакансии
        self.assertIn(self.vacancies[0], top_vacancies)  # Менеджер
        self.assertIn(self.vacancies[1], top_vacancies)  # Программист


if __name__ == '__main__':
    unittest.main()
