import unittest

from src.model.spreadsheet import Sheet


class SpreadsheetTestUnit1(unittest.TestCase):
    def testThatCellReferenceWorks(self):
        sheet = Sheet()
        sheet.put("A1", "8")
        sheet.put("A2", "=A1")
        self.assertEqual("8", sheet.get("A2"), "cell lookup")

        sheet.put("A1", "9")
        self.assertEqual("9", sheet.get("A2"), "cell change propagation")


    def testThatFormulasKnowCellsAndRecalculate(self):
        sheet = Sheet()
        sheet.put("A1", "8")
        sheet.put("A2", "3")
        sheet.put("B1", "=A1*(A1-A2)+A2/3")
        self.assertEqual("41", sheet.get("B1"), "calculation with cells")

        sheet.put("A2", "6")
        self.assertEqual("18", sheet.get("B1"), "re-calculation")

    def testThatDeepPropagationWorks(self):
        sheet = Sheet()
        sheet.put("A1", "8")
        sheet.put("A2", "=A1")
        sheet.put("A3", "=A2")
        sheet.put("A4", "=A3")
        self.assertEqual("8", sheet.get("A4"), "deep propagation")

        sheet.put("A2", "6")
        self.assertEqual("6", sheet.get("A4"), "deep re-calculation")

    def testThatFormulaWorksWithManyCells (self):
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
        sheet = Sheet()
        sheet.put("A1", "=A1")
        self.assertEqual("#Circular", sheet.get("A1"), "Detect circularity")