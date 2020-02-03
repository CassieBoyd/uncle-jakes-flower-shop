from arrangement import Arrangement

class MothersDay(Arrangement):

    def __init__(self):
        super().__init__()
        self.__flowers = []

    def enhance(self, flower):
        try:
            if flower.organic and flower.non_refridgerated and flower.stem_length == 4:
                self.__flowers.append(flower)
            else: 
                print(f'{flower.name} was not added to the arrangement.')
        except AttributeError: 
            print(f'{flower.name} cannot be added to this arrangement.')

    def listFlowers(self):
        print("Mother's Day Arrangement Fowers:")
        for flower in self.__flowers:
            print(flower.name)


    # Override the `enhance` method to ensure only
    # roses, lillies, and alstroemeria can be added