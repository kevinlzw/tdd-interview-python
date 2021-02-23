import unittest

from src.model.spreadsheet import Sheet


class SpreadsheetTestUnit1(unittest.TestCase):
    def testThatCellReferenceWorks(self):
        """
        Excel的等式应该正确地获取其他列的值
        """
        sheet = Sheet()
        sheet.put("A1", "8")
        sheet.put("A2", "=A1")
        self.assertEqual("8", sheet.get("A2"), "cell lookup")

        sheet.put("A1", "9")
        self.assertEqual("9", sheet.get("A2"), "cell change propagation")

    def testThatFormulasKnowCellsAndRecalculate(self):
        """
        Excel的等式应该正确地计算包含其他列的值的等式
        """
        sheet = Sheet()
        sheet.put("A1", "8")
        sheet.put("A2", "3")
        sheet.put("B1", "=A1*(A1-A2)+A2/3")
        self.assertEqual("41", sheet.get("B1"), "calculation with cells")

        sheet.put("A2", "6")
        self.assertEqual("18", sheet.get("B1"), "re-calculation")

    def testThatDeepPropagationWorks(self):
        """
        Excel的等式应该正确地获取其他列的值
        """
        sheet = Sheet()
        sheet.put("A1", "8")
        sheet.put("A2", "=A1")
        sheet.put("A3", "=A2")
        sheet.put("A4", "=A3")
        self.assertEqual("8", sheet.get("A4"), "deep propagation")

        sheet.put("A2", "6")
        self.assertEqual("6", sheet.get("A4"), "deep re-calculation")

    def testThatFormulaWorksWithManyCells(self):
        """
        Excel的等式应该正确地处理复杂的计算。
        """
        sheet = Sheet()
        sheet.put("A1", "10")
        sheet.put("A2", "=A1+B1")
        sheet.put("A3", "=A2+B2")
        sheet.put("A4", "=A3")
        sheet.put("B1", "7")
        sheet.put("B2", "=A2")
        sheet.put("B3", "=A3-A2")
        sheet.put("B4", "=A4+B3")

        self.assertEqual("34", sheet.get("A4"), "multiple expressions - A4")
        self.assertEqual("51", sheet.get("B4"), "multiple expressions - B4")

    def testThatCircularReferencesAdmitIt(self):
        """
        如果出现了循环引用，Excel应该提示。
        """
        sheet = Sheet()
        sheet.put("A1", "=A1")
        self.assertEqual("#Circular", sheet.get("A1"), "Detect circularity")
