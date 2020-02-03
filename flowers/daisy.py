from attributes import IOrganic, INonRefridgerated, IStemLength4


class Daisy(IOrganic, INonRefridgerated, IStemLength4):
    def __init__(self):
        IOrganic.__init__(self)
        INonRefridgerated.__init__(self)
        IStemLength4.__init__(self)
        self.name = "Daisy"