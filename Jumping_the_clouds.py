n = 7
cloud = [0, 1, 0, 0, 0, 1, 0]

if n <= 1:
    print(1)

no_of_jumps = 0
ptr = 0
for idx, i in enumerate(cloud):
    if idx < ptr:
        continue
    elif ptr == n-1:
        break
    if idx + 2 <= n-1 and cloud[idx+2] == 0:
        ptr = idx + 2
        print(idx, ptr, "jumping 2 steps")
    elif (idx + 2 <= n-1 and cloud[idx+2] == 1) or (idx + 1 <= n-1):
        ptr = idx + 1
        print(idx, ptr, "jumping 1 step")

    no_of_jumps = no_of_jumps + 1

print("no_of_jumps:", no_of_jumps)
