for i in range(5):
    print(i)

print()

for i in range(5):
    print(2*i)

print()

for _ in range(10):
    print("Hello")

print()

# ---------------------------

li = []

li.append("Burger")
li.append("Fries")
li.append("Soda")

print(li)

print(li[0])
print(li[-1])

li.append("Ice Cream")

print(li)

li.remove("Soda")

print(li)

li.pop(1)

print(li)

# ----------------------------

print()

print(len(li))

for i in range(len(li)):
    print(li[i])

print()

# -----------------------------
    
numbers = [1,2,3,4,5]

for i in range(len(numbers)):
    if numbers[i] == 3:
        print("The number 3 is in this list!")
    else:
        print("Current index is not equal to 3")


# ------------------------------
        
words = ["one", "two", "three", "four", "five"]

for i in range(len(words)):
    if words[i] is "three":
        print("Three is in this list")
    else:
        print("Current index is not 'three'")

# -------------------------------
        
number = 100

while number > 0:
    # number = number - 1
    number -= 1

print(number)

number2 = 500

# Modulo
while number2 % 7 != 0:
    number2 -= 1

print(number2)
