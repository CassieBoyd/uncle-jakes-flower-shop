from mothers_day import MothersDay
from valentines_day import ValentinesDay
from flowers import Alstroemeria, BabysBreath, Daisy, Lily, Poppy, Rose

# Valentine's Day flowers
alstroemeria = Alstroemeria()
lily = Lily()
red_rose = Rose("Red")

# Mother's Day flowers
babysbreath = BabysBreath()
daisy = Daisy()
poppy = Poppy()


for_mom = MothersDay()
for_mom.enhance(babysbreath)
for_mom.enhance(daisy)

# for_mom.enhance(alstroemeria)

print(for_mom.listFlowers)