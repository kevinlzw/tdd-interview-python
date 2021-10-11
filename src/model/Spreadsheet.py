class Sheet:

    def get(self, column: str):
        """
        该函数的目的是获取在column列的值，内容为等式的话需要计算并返回其结果。举例，若在"A1"列存储的值为"=7+3"，sheet.get("A1")应返回"10"。
        :param column: 列数
        :return: 该列存储的值，默认为空字符串
        """
        raise NotImplementedError("Not implemented!")

    def get_literal(self, column:str):
        """
        该函数的目的是获取在column列的字符串值，内容为等式的话不需要计算，直接返回字符串。举例，若在"A1"列存储的值为"=7+3"，sheet.getLiteral("A1")应返回"=7+3"。
        :param column: 列数
        :return: 该列存储的字符串值，默认为空字符串
        """
        raise NotImplementedError("Not implemented!")

    def put(self, column: str, value: str):
        """
        该函数的目的是在column列存储value的值。如果该列已经被占用，则替换为当前值。
        :param column: 列数
        :param value: 在该列需要存储的值
        """
        raise NotImplementedError("Not implemented!")