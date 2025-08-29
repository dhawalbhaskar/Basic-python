import os
import math

from fontTools.misc.cython import returns


def read_input(separator,input_str):
    imputdata = input("Enter {}  {} :".format(separator,input_str) )
    return imputdata

def create_dictionary():
    ## first space separated  to  key value
    data = read_input('space separated ','key and value')
    return  data.split()


def read_int():
   return int(input('enter a number which says following are space separated  key and value : '))

def check_dictionary(mydict,value):
    if value in mydict:
        return True
    else:
        return False

int_to_loop = range(read_int())
return_dict = {}
for i in int_to_loop:
    key,value = create_dictionary()
    return_dict[key] = value

input_val= read_input('as single value name ','to check ')
if check_dictionary(return_dict,input_val):
    print(return_dict[input_val])
else:
    print("{}  doesnt exits in dict {} ".format(input_val,return_dict))