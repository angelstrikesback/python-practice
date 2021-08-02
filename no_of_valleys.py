n = 8
input = "UDDDUDUUDUDDUDDUUU"


if n<=1:
    print(0)

level = 0
no_of_valley = 0

for i in input:
    if i == 'D':
        level = level - 1
    elif i == 'U':
        level = level + 1
        if level == 0:
            no_of_valley = no_of_valley + 1

print ("no of valleys:", no_of_valley)    
