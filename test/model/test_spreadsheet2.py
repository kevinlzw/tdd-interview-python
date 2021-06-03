import unittest

from src.model.spreadsheet import Sheet


class SpreadsheetTestUnit2(unittest.TestCase):
    def test_formula_spec(self):
        """
        对于格式不正确的等式(前面多了一个空格), Excel应该不予识别。
        """
        sheet = Sheet()
        sheet.put("B", " =7")
        self.assertEqual(" =7", sheet.get("B"), "Not a formula")
        self.assertEqual(" =7", sheet.getLiteral("B"), "Unchanged")

    def test_constant_formula(self):
        """
        Excel应该正确识别等式
        """
        sheet = Sheet()
        sheet.put("A", "=7")
        self.assertEqual("=7", sheet.getLiteral("A"), "Formula")
        self.assertEqual("7", sheet.get("A"), "Value")

    def test_parentheses(self):
        """
        Excel应该正确识别包含括号的等式
        """
        sheet = Sheet()
        sheet.put("A", "=(7)")
        self.assertEqual("7", sheet.get("A"), "Parenthesis")

    def test_deep_parentheses(self):
        """
        Excel应该正确识别包含很多括号的等式
        """
        sheet = Sheet()
        sheet.put("A", "=((((10))))")
        self.assertEqual("10", sheet.get("A"), "Parenthesis")

    def test_multiply(self):
        """
        Excel应该正确计算包含乘法的等式
        """
        sheet = Sheet()
        sheet.put("A", "=2*3*4")
        self.assertEqual("24", sheet.get("A"), "Times")

    def test_add(self):
        """
        Excel应该正确计算包含加法的等式
        """
        sheet = Sheet()
        sheet.put("A", "=71+2+3")
        self.assertEqual("76", sheet.get("A"), "Add")

    def test_procedence(self):
        """
        Excel应该根据先乘后加的顺序计算
        """
        sheet = Sheet()
        sheet.put("A", "=7+2*3")
        self.assertEqual("13", sheet.get("A"), "Procedence")

    def test_full_expression(self):
        """
        Excel应该正确地计算等式
        """
        sheet = Sheet()
        sheet.put("A", "=7*(2+3)*((((2+1))))")
        self.assertEqual("105", sheet.get("A"), "Expr")

    def test_simple_formula_error(self):
        """
        Excel应该返回错误信息若等式输入有错
        """
        sheet = Sheet()
        sheet.put("A", "=7*")
        self.assertEqual("#Error", sheet.get("A"), "Error")

    def test_parenthesis_error(self):
        """
        Excel应该返回错误信息若等式输入有错
        """
        sheet = Sheet()
        sheet.put("A", "=(((((7))")
        self.assertEqual("#Error", sheet.get("A"), "Error")