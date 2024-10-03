class dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} year old.")

    def make_sound(self):
        print("Bark")

class cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} year old.")

    def make_sound(self):
        print("Meow")

dog1 = dog("Sky",3)
cat1 = cat("Coco",4)

for animal in (dog1,cat1):
    animal.info()
    animal.make_sound()
    
