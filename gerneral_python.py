import os
import string
import math

## count freequency  in input list , i.e. [1,2,3,1,5,2,5,1,5] out put would be :{1:3,2:2,3:1 ... and so on.

def count_frequency(in_list):
    out = {}
    for num in in_list:
        out[num] = out.get(num, 0) + 1
    return out

outcome=count_frequency([1,2,3,1,5,2,5,1,5])
print(outcome)

##FizzBuzz problem

def fizbuzz(num):
    if num % 3 == 0 and  num % 5 == 0:
        return 'FizzBuzz'
    if num %3 ==0:
        return 'Fizz'
    elif num %5 ==0:
        return 'Buzz'
    else:
        return num

print(fizbuzz(4))

##find the largest int in  a list
def find_max(numlist):
    #first convert to set to get unique.
   # uniuq = set(numlist)
    return     max(numlist)

print(find_max([1,2,3,4,5,6,5,91  ,6]))
seq = [1,2,3,4,5,6,5,4,6]
def remove_duplicates(arr):
    return list(set(arr))
#as this  single line def,  lets try with lamda
rm_duplicate = (lambda arr: list(set(seq)) )(seq)

print(remove_duplicates(seq))

print(rm_duplicate)