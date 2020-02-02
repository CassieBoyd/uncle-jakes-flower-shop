from attributes import IOrganic, IRefridgerated, IStemLength7


class Lily(IOrganic, IRefridgerated, IStemLength7):
    def __init__(self,name):
        IOrganic.__init__(self)
        IRefridgerated.__init__(self)
        IStemLength7.__init__(self)
        self.name = name