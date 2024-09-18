import requests
from abc import ABC, abstractmethod


class JobAPI(ABC):
    @abstractmethod
    def get_vacancies(self, keyword: str) -> list:
        pass


class HeadHunterAPI(JobAPI):
    BASE_URL = "https://api.hh.ru/vacancies"  # Исправленный базовый URL

    def __init__(self):
        self.__headers = {"User-Agent": "HH-API-Client"}

    def __get(self, params: dict) -> dict:
        try:
            response = requests.get(self.BASE_URL, headers=self.__headers, params=params)
            response.raise_for_status()  # Проверяем статус-код
        except requests.exceptions.RequestException as e:
            raise Exception(f"Ошибка подключения: {e}")

        try:
            return response.json()  # Попытка распарсить JSON
        except requests.exceptions.JSONDecodeError:
            print("Ошибка декодирования JSON. Тело ответа сервера:")
            print(response.text)  # Логируем тело ответа
            raise Exception("Не удалось распарсить ответ от API в формате JSON.")

    def get_vacancies(self, keyword: str, per_page: int = 20) -> list:
        params = {"text": keyword, "per_page": per_page}
        data = self.__get(params)
        return data.get("items", [])
