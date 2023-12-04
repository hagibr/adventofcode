input = '''Frosting: capacity 4, durability -2, flavor 0, texture 0, calories 5
Candy: capacity 0, durability 5, flavor -1, texture 0, calories 8
Butterscotch: capacity -1, durability 0, flavor 5, texture 0, calories 6
Sugar: capacity 0, durability 0, flavor -2, texture 2, calories 1'''

# Parsing ingredients list
ingredient = []
for entry in input.splitlines():
  entry = entry.replace(": capacity", "").replace(", durability", "").replace(", flavor", "").replace(", texture", "").replace(", calories", "").split()
  ingredient.append( [entry[0], int(entry[1]), int(entry[2]), int(entry[3]), int(entry[4]), int(entry[5])])

# print(ingredient)

# Answers for each part
best_score = 0
best_500cal_score = 0

# Trying every permutation (100^3)
for frosting in range(100):
  for candy in range(100):
    for butterscotch in range(100):
      # This way we guarantee that the ingredients sum to 100 teaspoons
      sugar = 100 - butterscotch - candy - frosting

      # Calculating the totals of every category
      total_capacity = ingredient[0][1]*frosting + ingredient[1][1]*candy + ingredient[2][1]*butterscotch + ingredient[3][1]*sugar
      total_durability = ingredient[0][2]*frosting + ingredient[1][2]*candy + ingredient[2][2]*butterscotch + ingredient[3][2]*sugar
      total_flavor = ingredient[0][3]*frosting + ingredient[1][3]*candy + ingredient[2][3]*butterscotch + ingredient[3][3]*sugar
      total_texture = ingredient[0][4]*frosting + ingredient[1][4]*candy + ingredient[2][4]*butterscotch + ingredient[3][4]*sugar
      # The lowest we can go is zero
      total_capacity = max(total_capacity, 0)
      total_durability = max(total_durability, 0)
      total_flavor = max(total_flavor, 0)
      total_texture = max(total_texture, 0)
      
      # Part One is here
      total_score = total_capacity*total_durability*total_flavor*total_texture
      best_score = max(total_score, best_score)
      
      # Part two is here
      total_calories = ingredient[0][5]*frosting + ingredient[1][5]*candy + ingredient[2][5]*butterscotch + ingredient[3][5]*sugar
      if( total_calories == 500 ):
        best_500cal_score = max(total_score, best_500cal_score)

print(f"Part One: {best_score}")

print(f"Part Two: {best_500cal_score}")
