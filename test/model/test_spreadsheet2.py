import unittest

from src.model.spreadsheet import Sheet


class SpreadsheetTestUnit1(unittest.TestCase):
    def testFormulaSpec(self):
        sheet = Sheet()
        sheet.put("B1", " =7")
        self.assertEqual(" =7", sheet.get("B1"), "Not a formula")
        self.assertEqual(" =7", sheet.getLiteral("B1"), "Unchanged")

    def testConstantFormula(self):
        sheet = Sheet()
        sheet.put("A1", "=7")
        self.assertEqual("=7", sheet.getLiteral("B1"), "Formula")
        self.assertEqual("7", sheet.get("B1"), "Value")

    def testParentheses(self):
        sheet = Sheet()
        sheet.put("A1", "=(7)")
        self.assertEqual("7", sheet.get("A1"), "Parenthesis")

    def testDeepParentheses(self):
        sheet = Sheet()
        sheet.put("A1", "=((((10))))")
        self.assertEqual("10", sheet.get("A1"), "Parenthesis")

    def testMultiply(self):
        sheet = Sheet()
        sheet.put("A1", "=2*3*4")
        self.assertEqual("24", sheet.get("A1"), "Times")

    def testAdd(self):
        sheet = Sheet()
        sheet.put("A1", "=71+2+3")
        self.assertEqual("76", sheet.get("A1"), "Add")

    def testProcedence(self):
        sheet = Sheet()
        sheet.put("A1", "=7+2*3")
        self.assertEqual("13", sheet.get("A1"), "Procedence")

    def testFullExpression(self):
        sheet = Sheet()
        sheet.put("A1", "=7*(2+3)*((((2+1))))")
        self.assertEqual("105", sheet.get("A1"), "Expr")

    def testSimpleFormulaError(self):
        sheet = Sheet()
        sheet.put("A1", "=7*")
        self.assertEqual("#Error", sheet.get("A1"), "Error")

    def testParenthesisError(self):
        sheet = Sheet()
        sheet.put("A1", "=(((((7))")
        self.assertEqual("#Error", sheet.get("A1"), "Error")