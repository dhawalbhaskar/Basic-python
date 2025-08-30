import os

#t = lambda num: num*2

seq  = list(range(0,10,2))
outcome = list(map(lambda num : num **2 ,seq))
print(outcome)
out = list(filter(lambda num : num % 2 == 0, seq))
print(out)