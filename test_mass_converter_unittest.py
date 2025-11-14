import pytest
from unittest.mock import patch
from mass_converter import main


# Вспомогательная функция для проверки вывода print

def printed_contains(mock_print, substring):
    """
    Проверяет, что любая строка, переданная в print, содержит подстроку substring.
    Работает для любых вызовов print, включая tuple аргументы.
    """
    for call in mock_print.call_args_list:
        # Каждое обращение к print может быть с tuple аргументов
        if any(substring in str(arg) for arg in call[0]):
            return True
    return False



# Тесты main() с mock


def test_main_valid_conversion():
    user_inputs = ["10", "кг", "фунт"]
    with patch("builtins.input", side_effect=user_inputs), patch("builtins.print") as mock_print:
        main()
        # Проверяем, что результат конвертации присутствует в выводе
        assert printed_contains(mock_print, "10.0 кг = 22.0462 фунт")


def test_main_negative_mass():
    user_inputs = ["-5", "кг", "фунт"]
    with patch("builtins.input", side_effect=user_inputs), patch("builtins.print") as mock_print:
        main()
        assert printed_contains(mock_print, "Масса не может быть отрицательной.")


def test_main_invalid_value():
    user_inputs = ["abc", "кг", "фунт"]
    with patch("builtins.input", side_effect=user_inputs), patch("builtins.print") as mock_print:
        main()
        assert printed_contains(mock_print, "Ошибка: введите корректное число.")


def test_main_unknown_unit():
    user_inputs = ["10", "неизвестно", "кг"]
    with patch("builtins.input", side_effect=user_inputs), patch("builtins.print") as mock_print:
        main()
        # Проверяем, что текст ошибки с неизвестной единицей есть в любом вызове print
        assert printed_contains(mock_print, "Неизвестная исходная единица")
