from mothers_day import MothersDay
from valentines_day import ValentinesDay
from flowers import Alstroemeria, BabysBreath, Daisy, Lily, Poppy, RedRose, BlueRose, PinkRose

# Valentine's Day flowers
alstroemeria = Alstroemeria()
lily = Lily()
red_rose = RedRose()
blue_rose = BlueRose()
pink_rose = PinkRose()

# Mother's Day flowers
babysbreath = BabysBreath()
daisy = Daisy()
poppy = Poppy()


for_mom = MothersDay()
for_mom.enhance(babysbreath)
for_mom.enhance(daisy)
for_mom.enhance(poppy)
# for_mom.enhance(blue_rose)
# for_mom.enhance(alstroemeria)
for_mom.listFlowers()

for_wife = ValentinesDay()
for_wife.enhance(red_rose)
for_wife.enhance(pink_rose)
for_wife.enhance(blue_rose)
for_wife.enhance(lily)
for_wife.enhance(alstroemeria)
for_wife.listFlowers()