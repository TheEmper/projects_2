import math

def infected(days):
    computers = 1

    for num in range(0, days):
        computers *= 2
        if (num + 1) % 3 == 0:
            patched = math.ceil(computers * 0.2)
            computers = computers - patched
    return computers

print(infected(25))