from arrangement import Arrangement

class MothersDay(Arrangement):

    def __init__(self, flower):
        super().__init__(flower)
        self.__flowers = []

    def enhance(self, flower):
        if flower.organic and flower.non_refridgerated and flower.stem_length_4:
            self.__flowers.append(flower)
        else: 
            print(f'{flower.name} cannot be added to this arrangement.')


    # Override the `enhance` method to ensure only
    # roses, lillies, and alstroemeria can be added