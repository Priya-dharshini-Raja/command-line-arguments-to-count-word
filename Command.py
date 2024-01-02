#program is developed: Priyadharshini Raja
# REF.NO: 23013908

import sys
count= 0
with open(sys.argv[1],'r') as file:
    for line in file:
        word= line.split()
        count += len(word)
print("program is developed: Pavithra R")
print("word count in file = ",count)
