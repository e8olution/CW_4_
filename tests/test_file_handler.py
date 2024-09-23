import unittest
import os
import json
from src.file_handler import JSONSaver
from src.vacancies import Vacancy  # Предполагается, что класс Vacancy уже определен


class TestJSONSaver(unittest.TestCase):

    def setUp(self):
        self.saver = JSONSaver("test_vacancies.json")  # Используем тестовый файл
        self.vacancy1 = Vacancy(title="Менеджер", link="https://example.com/1", salary={"from": 50000},
                                description="Работа с клиентами", requirements="Опыт работы с клиентами")
        self.vacancy2 = Vacancy(title="Программист", link="https://example.com/2", salary={"from": 80000},
                                description="Знания Python", requirements="Опыт разработки на Python")

    def tearDown(self):
        # Удаляем тестовый файл после каждого теста
        if os.path.exists("test_vacancies.json"):
            os.remove("test_vacancies.json")

    def test_add_vacancy(self):
        self.saver.add_vacancy(self.vacancy1)
        with open("test_vacancies.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            self.assertEqual(len(data), 1)
            self.assertEqual(data[0]["title"], "Менеджер")

    def test_get_vacancies(self):
        self.saver.add_vacancy(self.vacancy1)
        self.saver.add_vacancy(self.vacancy2)
        vacancies = self.saver.get_vacancies()
        self.assertEqual(len(vacancies), 2)

    def test_delete_vacancy(self):
        self.saver.add_vacancy(self.vacancy1)
        self.saver.add_vacancy(self.vacancy2)
        self.saver.delete_vacancy(self.vacancy1)
        vacancies = self.saver.get_vacancies()
        self.assertEqual(len(vacancies), 1)
        self.assertEqual(vacancies[0]["title"], "Программист")

    def test_save_vacancies_to_file(self):
        self.saver.add_vacancy(self.vacancy1)
        self.saver.add_vacancy(self.vacancy2)
        self.saver.save_vacancies_to_file([self.vacancy1, self.vacancy2])

        with open("test_vacancies.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            self.assertEqual(len(data), 2)
            self.assertEqual(data[0]["title"], "Менеджер")
            self.assertEqual(data[1]["title"], "Программист")


if __name__ == '__main__':
    unittest.main()
