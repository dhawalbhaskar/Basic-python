from itertools import permutations
from itertools import combinations
x=y=z=1
n=2
coordinates = [
  [i, j, k]
  for i in range(x + 1)
  for j in range(y + 1)
  for k in range(z + 1)
  if i + j + k != n

]
print(coordinates)

