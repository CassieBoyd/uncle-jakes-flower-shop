from arrangement import Arrangement
class ValentinesDay(Arrangement):
    def __init__(self):
        super().__init__()
        self.__flowers = []

    def enhance(self, flower):
        try:
            if flower.non_organic and flower.refridgerated and flower.stem_length == 7:
                self.__flowers.append(flower)
            else: 
                print(f'{flower.name} was not added to the arrangement.')
        except AttributeError: 
            print(f'{flower.name} cannot be added to this arrangement.')

    def listFlowers(self):
        print("Valentine's Day Arrangement Flowers:")
        for flower in self.__flowers:
            print(flower.name)