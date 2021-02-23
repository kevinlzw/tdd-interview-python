class Sheet:

    def get(self, s: str):
        raise NotImplementedError("Not implemented!")

    def getLiteral(self, s:str):
        raise NotImplementedError("Not implemented!")

    def put(self, cell: str, s: str):
        raise NotImplementedError("Not implemented!")