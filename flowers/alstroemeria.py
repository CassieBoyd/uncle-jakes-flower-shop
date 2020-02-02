from attributes import IOrganic, IRefridgerated, IStemLength

class Alstroemeria(IOrganic, IRefridgerated, IStemLength):
    def __init__(self,name):
        super().__init__()
        self.name = name