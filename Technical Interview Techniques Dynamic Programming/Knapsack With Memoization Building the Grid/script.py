from util import Loot

def knapsack(loot, weight_limit):
  grid = [[0 for col in range(weight_limit + 1)] for row in range(len(loot) + 1)]
  for row, item in enumerate(loot):
    row = row + 1
    for col in range(weight_limit + 1):
      weight_capacity = col
  return grid
    
available_loot = [Loot("Clock", 3, 8), Loot("Vase", 4, 12), Loot("Diamond", 1, 7)]
weight_capacity = 4
best_combo = knapsack(available_loot, weight_capacity)
print("The ideal loot given capacity {0} is\n{1}".format(weight_capacity, best_combo))
