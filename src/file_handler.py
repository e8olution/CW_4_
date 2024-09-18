import json
from abc import ABC, abstractmethod


class FileHandler (ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies(self) -> list:
        pass


class JSONSaver (FileHandler):
    def __init__(self, file_name="data/vacancies.json"):
        self.__file_name = file_name

    def add_vacancy(self, vacancy):
        vacancies = self.get_vacancies()
        vacancies.append(vacancy.__dict__)
        with open(self.__file_name, 'w', encoding='utf-8') as f:
            json.dump(vacancies, f, ensure_ascii=False, indent=4)

    def delete_vacancy(self, vacancy):
        vacancies = self.get_vacancies()
        vacancies = [v for v in vacancies if v['url'] != vacancy.url]
        with open(self.__file_name, 'w', encoding='utf-8') as f:
            json.dump(vacancies, f, ensure_ascii=False, indent=4)

    def get_vacancies(self) -> list:
        try:
            with open(self.__file_name, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
