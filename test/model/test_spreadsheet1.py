import unittest

from src.model.spreadsheet import Sheet


class SpreadsheetTestUnit1(unittest.TestCase):
    def testThatCellsAreEmptyByDefault(self):
        sheet = Sheet()
        self.assertEqual("", sheet.get("A1"))
        self.assertEqual("", sheet.get("ZX347"))

    def testThatTextCellsAreStored(self):
        sheet = Sheet()
        cell = 'A21'

        sheet.put(cell, "A string")
        self.assertEqual("A string", sheet.get(cell))

        sheet.put(cell, "A different string")
        self.assertEqual("A different string", sheet.get(cell))

        sheet.put(cell, "")
        self.assertEqual("", sheet.get(cell))

    def testThatManyCellsExist(self):
        sheet = Sheet()
        sheet.put("A1", "First")
        sheet.put("X27", "Second")
        sheet.put("ZX901", "Third")

        self.assertEqual("First", sheet.get("A1"), "A1")
        self.assertEqual("Second", sheet.get("X27"), "X27")
        self.assertEqual("Third", sheet.get("ZX901"), "ZX901")

        sheet.put("A1", "Fourth")
        self.assertEqual("Fourth", sheet.get("A1"), "A1 after")
        self.assertEqual("Second", sheet.get("X27"), "X27 same")
        self.assertEqual("Third", sheet.get("ZX901"), "ZX901 same")

    def testThatNumericCellsAreIdentifiedAndStored(self):
        sheet = Sheet()
        cell = 'A21'

        sheet.put(cell, "X99")
        self.assertEqual("X99", sheet.get(cell))

        sheet.put(cell, "14")
        self.assertEqual("14", sheet.get(cell))

        sheet.put(cell, " 99 X")
        self.assertEqual(" 99 X", sheet.get(cell))

        sheet.put(cell, " 1234 ")
        self.assertEqual("1234", sheet.get(cell))

        sheet.put(cell, " ")
        self.assertEqual(" ", sheet.get(cell))

    def testThatWeHaveAccessToCellLiteralValuesForEditing(self):
        sheet = Sheet()
        cell = 'A21'

        sheet.put(cell, "Some string")
        self.assertEqual("Some string", sheet.getLiteral(cell))

        sheet.put(cell, " 1234 ")
        self.assertEqual(" 1234 ", sheet.getLiteral(cell))

        sheet.put(cell, "=7")
        self.assertEqual("=7", sheet.getLiteral(cell))