from attributes import INonOrganic, IRefridgerated, IStemLength7


# Note that when a class inherits from two parents that you have to discard using the super().__init__() syntax and explicitly invoke the initialization method of both. You also need to pass self as an argument - something that is not needed when you use the super() abstraction.
class Alstroemeria(INonOrganic, IRefridgerated, IStemLength7):
    def __init__(self):
        INonOrganic.__init__(self)
        IRefridgerated.__init__(self)
        IStemLength7.__init__(self)
        self.name = "Alstroemeria"