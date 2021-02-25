import unittest

from src.model.spreadsheet import Sheet


class SpreadsheetTestUnit1(unittest.TestCase):
    def testThatCellsAreEmptyByDefault(self):
        """
        每列默认值为空字符串
        """
        sheet = Sheet()
        self.assertEqual("", sheet.get("A"))
        self.assertEqual("", sheet.get("ZX"))

    def testThatTextCellsAreStored(self):
        """
        Excel可以正确地存储put的值
        """
        sheet = Sheet()
        cell = 'A'

        sheet.put(cell, "A string")
        self.assertEqual("A string", sheet.get(cell))

        sheet.put(cell, "A different string")
        self.assertEqual("A different string", sheet.get(cell))

        sheet.put(cell, "")
        self.assertEqual("", sheet.get(cell))

    def testThatManyCellsExist(self):
        """
        Excel可以正确地覆盖之前的值
        """
        sheet = Sheet()
        sheet.put("A", "First")
        sheet.put("X", "Second")
        sheet.put("ZX", "Third")

        self.assertEqual("First", sheet.get("A"), "A")
        self.assertEqual("Second", sheet.get("X"), "X")
        self.assertEqual("Third", sheet.get("ZX"), "ZX")

        sheet.put("A", "Fourth")
        self.assertEqual("Fourth", sheet.get("A"), "A after")
        self.assertEqual("Second", sheet.get("X"), "X same")
        self.assertEqual("Third", sheet.get("ZX"), "ZX same")

    def testThatNumericCellsAreIdentifiedAndStored(self):
        """
        Excel可以正确识别纯数字，对于纯数字，将多余的空格去掉。
        """
        sheet = Sheet()
        cell = 'A'

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
        """
        getLiteral需要返回未处理的纯字符串。
        """
        sheet = Sheet()
        cell = 'A'

        sheet.put(cell, "Some string")
        self.assertEqual("Some string", sheet.getLiteral(cell))

        sheet.put(cell, " 1234 ")
        self.assertEqual(" 1234 ", sheet.getLiteral(cell))

        sheet.put(cell, "=7")
        self.assertEqual("=7", sheet.getLiteral(cell))