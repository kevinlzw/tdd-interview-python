import unittest

from src.model.spreadsheet import Sheet


class SpreadsheetTestUnit3(unittest.TestCase):
    def testThatCellReferenceWorks(self):
        """
        Excel的等式应该正确地获取其他列的值
        """
        sheet = Sheet()
        sheet.put("A", "8")
        sheet.put("B", "=A")
        self.assertEqual("8", sheet.get("B"), "cell lookup")

        sheet.put("A", "9")
        self.assertEqual("9", sheet.get("B"), "cell change propagation")

    def testThatFormulasKnowCellsAndRecalculate(self):
        """
        Excel的等式应该正确地计算包含其他列的值的等式
        """
        sheet = Sheet()
        sheet.put("A", "8")
        sheet.put("B", "3")
        sheet.put("E", "=A*(A-B)+B/3")
        self.assertEqual("41", sheet.get("E"), "calculation with cells")

        sheet.put("B", "6")
        self.assertEqual("18", sheet.get("E"), "re-calculation")

    def testThatDeepPropagationWorks(self):
        """
        Excel的等式应该正确地获取其他列的值
        """
        sheet = Sheet()
        sheet.put("A", "8")
        sheet.put("B", "=A")
        sheet.put("C", "=B")
        sheet.put("D", "=C")
        self.assertEqual("8", sheet.get("D"), "deep propagation")

        sheet.put("B", "6")
        self.assertEqual("6", sheet.get("D"), "deep re-calculation")

    def testThatFormulaWorksWithManyCells(self):
        """
        Excel的等式应该正确地处理复杂的计算。
        """
        sheet = Sheet()
        sheet.put("A", "10")
        sheet.put("B", "=A+E")
        sheet.put("C", "=B+F")
        sheet.put("D", "=C")
        sheet.put("E", "7")
        sheet.put("F", "=B")
        sheet.put("G", "=C-B")
        sheet.put("H", "=D+G")

        self.assertEqual("34", sheet.get("D"), "multiple expressions - D")
        self.assertEqual("51", sheet.get("H"), "multiple expressions - H")

    def testThatCircularReferencesAdmitIt(self):
        """
        如果出现了循环引用，Excel应该提示。
        """
        sheet = Sheet()
        sheet.put("A", "=A")
        self.assertEqual("#Circular", sheet.get("A"), "Detect circularity")
