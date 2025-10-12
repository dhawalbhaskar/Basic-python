import re
import string



def reverse_str(words)->str:
    result = ""
    for char in words:
        result = char + result
    return result
print(reverse_str(words='abccba'))

# remove all  consonant :
def remove_Consonants(in_string)->str:
    pattern = r'[^aeiouAEIOU]'
    return re.sub(pattern,'',in_string)

print (remove_Consonants('bci123do'))

def remove_without_Cons_re(in_string)->str:
    vowels = 'aeiouAEIOU'
    result = [char for char in in_string if not char.isalpha() or   char in vowels]
    return ''.join(result)
print(remove_without_Cons_re('Python And Data 2 Science 3'))

def is_prime(num):
    for z in range(2,num):
        if num % z == 0:
            return False
    return True


def sum_prime(in_num)->int:
    sum = 0
    for num in range(2,in_num+1):
        if is_prime(num):
            sum += num
    return sum


print (sum_prime(10))