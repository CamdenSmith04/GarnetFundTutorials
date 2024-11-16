def add(int1, int2):
    return int1 + int2

print(add(5, 12), end="\n\n")

# ------------------------------

def multiply(int1, int2, int3):
    product = int1*int2*int3
    print(f"{int1} * {int2} * {int3} = {product}")
    return

multiply(5, 2, 7)

# ------------------------------

def subtract_until_ten(x):
    if x == 10:
        return x
    elif x > 10:
        return subtract_until_ten(x-1)
    else:
        return "Number is below ten"

print(subtract_until_ten(100))
print(subtract_until_ten(5))