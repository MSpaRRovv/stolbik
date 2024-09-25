import unittest
from main import stolbik


class TestStolbik(unittest.TestCase):
    def test_division(self):
        test_cases = [
            (10, 2, 5, 0),  # 10 делим на 2, результат 5, остаток 0
            (15, 4, 3, 3),  # 15 делим на 4, результат 3, остаток 3
            (28, 5, 5, 3),  # 28 делим на 5, результат 5, остаток 3
            (1000, 10, 100, 0),  # 100 делим на 10, результат 10, остаток 0
            (50, 7, 7, 1),  # 50 делим на 7, результат 7, остаток 1
            (9, 3, 3, 0),  # 9 делим на 3, результат 3, остаток 0
            (27, 4, 6, 3),  # 27 делим на 4, результат 6, остаток 3
            (81, 9, 9, 0),  # 81 делим на 9, результат 9, остаток 0
            (77, 10, 7, 7),  # 77 делим на 10, результат 7, остаток 7
            (200, 33, 6, 2),  # 200 делим на 33, результат 6, остаток 2
        ]

        for num, div, expected_result, expected_remainder in test_cases:
            with self.subTest(num=num, div=div):
                result, remainder = stolbik(num, div)  # Вызываем функцию и получаем результат и остаток

                # Проверяем результат и остаток
                self.assertEqual(result, expected_result)
                self.assertEqual(remainder, expected_remainder)



