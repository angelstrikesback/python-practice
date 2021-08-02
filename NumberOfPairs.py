input = [1, 2, 3, 4, 5, 5, 5, 5, 1, 2, 1, 1, 1]

if not input or len(input) <= 1:
    print(0)

seen = {}

no_of_pairs = 0

for i in input:
    if i in seen:
        no_of_pairs = no_of_pairs + 1
        del seen[i]
    else:
        seen[i] = i

print("Number of pairs:", no_of_pairs)

