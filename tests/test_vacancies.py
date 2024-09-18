import unittest
from src.vacancy import Vacancy


class TestVacancy(unittest.TestCase):
    def test_vacancy_init(self):
        vacancy = Vacancy("Python Developer", "https://hh.ru/vacancy/123", "100 000-150 000 руб.",
                          "Требования: опыт работы")
        self.assertEqual(vacancy.title, "Python Developer")
        self.assertEqual(vacancy.url, "https://hh.ru/vacancy/123")

    def test_salary_comparison(self):
        vacancy1 = Vacancy("Python Developer", "https://hh.ru/vacancy/123", "100 000-150 000 руб.",
                           "Требования: опыт работы")
        vacancy2 = Vacancy("Java Developer", "https://hh.ru/vacancy/124", "150 000-200 000 руб.",
                           "Требования: опыт работы")
        self.assertTrue(vacancy2 > vacancy1)
