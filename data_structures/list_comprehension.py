import numpy as np
import math, random


flowers = ["daisy", "rose", "tulip", "peony", "daffidil"]

gt_four_list = [i for i in flowers if len(i) > 4]
print(gt_four_list)

swapcase = [x.swapcase() for x in flowers]

nums = random.seed(40)

num_list = [num for num in nums if num < 1]
