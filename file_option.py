import os

## open a file with option

with open('example.txt', 'r') as readfile:
    with open('example2.txt', 'w') as writefile:
        for line in readfile:
            writefile.write(line)

