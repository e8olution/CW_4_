import unittest
from unittest.mock import patch, Mock
from src.api import HH


class TestHH(unittest.TestCase):

    @patch('src.api.requests.get')
    def test_load_vacancies_success(self, mock_get):
        # Настройка мок-ответа
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'items': [
                {'id': '1', 'name': 'Менеджер по туризму'},
                {'id': '2', 'name': 'Программист'},
            ]
        }
        mock_get.return_value = mock_response

        hh = HH()
        vacancies = hh.load_vacancies("Курьер")

        self.assertEqual(len(vacancies), 2)
        self.assertEqual(vacancies[0]['name'], 'Менеджер по туризму')
        self.assertEqual(vacancies[1]['name'], 'Программист')

    @patch('src.api.requests.get')
    def test_load_vacancies_failure(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        hh = HH()
        vacancies = hh.load_vacancies("Курьер")

        self.assertEqual(len(vacancies), 0)

    @patch('src.api.requests.get')
    def test_load_vacancies_partial_success(self, mock_get):
        mock_response_success = Mock()
        mock_response_success.status_code = 200
        mock_response_success.json.return_value = {
            'items': [{'id': '1', 'name': 'Менеджер по туризму'}]
        }

        mock_response_empty = Mock()
        mock_response_empty.status_code = 200
        mock_response_empty.json.return_value = {
            'items': []
        }

        mock_get.side_effect = [mock_response_success,
                                mock_response_empty]

        hh = HH()
        vacancies = hh.load_vacancies("Курьер")

        self.assertEqual(len(vacancies), 1)
        self.assertEqual(vacancies[0]['name'], 'Менеджер по туризму')


if __name__ == '__main__':
    unittest.main()
