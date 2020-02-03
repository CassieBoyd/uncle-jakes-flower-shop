from .rose import Rose

class RedRose(Rose):
    def __init__(self):
        super().__init__()
        self.color = "Red"
        self.name = "Red Rose"