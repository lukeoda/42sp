import sys


param_1= sys.argv[1] 

for x in range(11):
    prod = int(param_1) * int(x)
    print(str(x) + ' x ' + param_1 + ' = ' + str(prod));

