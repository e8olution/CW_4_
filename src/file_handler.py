import json
import os
from abc import ABC, abstractmethod


class VacancyFileConnector(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies(self, criteria=None):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass

    @abstractmethod
    def save_vacancies_to_file(self, vacancies):
        pass


class JSONSaver(VacancyFileConnector):
    def __init__(self, filename="data/vacancies.json"):
        self.filename = filename
        if not os.path.exists(self.filename):
            self._create_empty_file()

    def _create_empty_file(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump([], file)

    def _load_data(self):
        with open(self.filename, 'r', encoding='utf-8') as file:
            return json.load(file)

    def _save_data(self, data):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def add_vacancy(self, vacancy):
        data = self._load_data()
        data.append({
            "title": vacancy.title,
            "url": vacancy.link,
            "salary": vacancy.salary,
            "description": vacancy.description
        })
        self._save_data(data)

    def get_vacancies(self, criteria=None):
        data = self._load_data()
        if criteria is None:
            return data
        return [vacancy for vacancy in data if all(criteria[key] in str(vacancy.get(key, "")) for key in criteria)]

    def delete_vacancy(self, vacancy):
        data = self._load_data()
        data = [item for item in data if item["url"] != vacancy.link]  # Изменено с vacancy.url на vacancy.link
        self._save_data(data)

    def save_vacancies_to_file(self, vacancies):
        # Убедимся, что vacancies - это список
        if not isinstance(vacancies, list):
            raise ValueError("Expected a list of vacancies")

        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump([vacancy.__dict__ for vacancy in vacancies], f, ensure_ascii=False, indent=4)
