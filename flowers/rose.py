from attributes import INonOrganic, IRefridgerated, IStemLength7

class Rose(INonOrganic, IRefridgerated, IStemLength7):
    def __init__(self, name, color):
        INonOrganic.__init__(self)
        IRefridgerated.__init__(self)
        IStemLength7.__init__(self)
        self.name = name
        self.color = ["red", "pink", "blue"]

# if __name__ == "__main__":
#     for_beth = ValentinesDay()
#     red_rose = Rose()

#     for_beth.flowers.append(red_rose)