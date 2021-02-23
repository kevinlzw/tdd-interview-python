class Sheet:

    def get(self, column: str):
        raise NotImplementedError("Not implemented!")

    def getLiteral(self, column:str):
        raise NotImplementedError("Not implemented!")

    def put(self, column: str, value: str):
        raise NotImplementedError("Not implemented!")