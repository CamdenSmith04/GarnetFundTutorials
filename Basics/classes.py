class Animal:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
    
    def is_faster_than(self, animal2):
        if self.speed > animal2.speed:
            print(f"{self.name} is faster than {animal2.name}")
        elif self.speed < animal2.speed:
            print(f"{self.name} is slower than {animal2.name}")
        else:
            print("The animals are the same speed")


Cat = Animal("Cat", 50)
Dog = Animal("Dog", 75)
Cheetah = Animal("Cheetah", 200)

print(Cat.name)
print(Cat.speed)

Cat.is_faster_than(Dog)
Cheetah.is_faster_than(Dog)