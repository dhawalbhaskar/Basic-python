from itertools import permutations

### in put number of
# ## in put  an n  out put will be  number of unique  one., of square one , for example

##for example n is 10 then  it will be (4,3,5) as 4 **2 = 16 + 9 = 25 that is sqaure of 5, same as

# so as lets say :  then  for range n, , a**2 + b**2 = c**2


def read_input():
    n = int(input('enter value of number \n'))
    return n


def pythagorean_permutations(num):
    result = []
    for param in permutations(num,3):
        a, b, c = param
        if a**2 + b**2 == c**2:
            result.append((a,b,c))
    return result

n=read_input()
numlist = range(1,n+1)
print (pythagorean_permutations(numlist))

