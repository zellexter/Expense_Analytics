import unittest
from Expenses_Code import Expense_Visualization

class TestExpenseVisualization(unittest.TestCase):

    def setUp(self):
        self.expense_viz = Expense_Visualization('a','b')

    def test_expense_visualization_instance(self):
        self.assertIsInstance(self.expense_viz, Expense_Visualization)

    def test_expense_visualization_attributes(self):
        expected_attributes = ['data', 'categories', 'amounts']
        for attr in expected_attributes:
            self.assertTrue(hasattr(self.expense_viz, attr), f"Expense_Visualization should have a '{attr}' attribute")

    def test_expense_visualization_methods(self):
        expected_methods = ['load_data', 'generate_pie_chart', 'generate_bar_chart', 'generate_line_chart']
        for method in expected_methods:
            self.assertTrue(hasattr(self.expense_viz, method) and callable(getattr(self.expense_viz, method)), 
                            f"Expense_Visualization should have a '{method}' method")

    def test_load_data_empty(self):
        with self.assertRaises(ValueError):
            self.expense_viz.load_data([])

    def test_load_data_invalid_format(self):
        invalid_data = [{'invalid_key': 'value'}]
        with self.assertRaises(KeyError):
            self.expense_viz.load_data(invalid_data)

    def test_generate_pie_chart_no_data(self):
        with self.assertRaises(ValueError):
            self.expense_viz.generate_pie_chart()

    def test_generate_bar_chart_no_data(self):
        with self.assertRaises(ValueError):
            self.expense_viz.generate_bar_chart()

    def test_generate_line_chart_no_data(self):
        with self.assertRaises(ValueError):
            self.expense_viz.generate_line_chart()

if __name__ == '__main__':
    unittest.main()
