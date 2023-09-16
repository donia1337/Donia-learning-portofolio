# You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall.

print("Hey! I see you need little help to figure out how many cans of pain you need to cover your walls.\nLet me help you!")

import math

def paint_calc(height, width, cover):
    num_cans = (height * width) / cover
    round_cans = math.ceil(num_cans)
    print(f"You will need {round_cans} cans to pint your walls.")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)



