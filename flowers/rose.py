from attributes import INonOrganic, IRefridgerated, IStemLength7

class Rose(INonOrganic, IRefridgerated, IStemLength7):
    def __init__(self):
        INonOrganic.__init__(self)
        IRefridgerated.__init__(self)
        IStemLength7.__init__(self)
        self.name = "Rose"
            
