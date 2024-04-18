import unittest

import validate_input

class TestInputValidation(unittest.TestCase):
    def test_symbol_valid(self):
        self.assertTrue(validate_input('AAPL', '1', '1', '2022-01-01', '2022-01-10'))

    def test_symbol_invalid(self):
        self.assertFalse(validate_input('aapl', '1', '1', '2022-01-01', '2022-01-10'))

    def test_chart_type_valid(self):
        self.assertTrue(validate_input('AAPL', '1', '1', '2022-01-01', '2022-01-10'))

    def test_chart_type_invalid(self):
        self.assertFalse(validate_input('AAPL', '3', '1', '2022-01-01', '2022-01-10'))

    def test_time_series_valid(self):
        self.assertTrue(validate_input('AAPL', '1', '1', '2022-01-01', '2022-01-10'))

    def test_time_series_invalid(self):
        self.assertFalse(validate_input('AAPL', '1', '5', '2022-01-01', '2022-01-10'))

    def test_start_date_valid(self):
        self.assertTrue(validate_input('AAPL', '1', '1', '2022-01-01', '2022-01-10'))

    def test_start_date_invalid(self):
        self.assertFalse(validate_input('AAPL', '1', '1', '01-01-2022', '2022-01-10'))

    def test_end_date_valid(self):
        self.assertTrue(validate_input('AAPL', '1', '1', '2022-01-01', '2022-01-10'))

    def test_end_date_invalid(self):
        self.assertFalse(validate_input('AAPL', '1', '1', '2022-01-01', '10-01-2022'))

if __name__ == '__main__':
    unittest.main()
