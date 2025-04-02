"""
Converting Java to Python
"""

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def GetName(self):
        return self.name

    def GetAge(self):
        return self.age

    def speak(self):
        return f"{self.name} makes a sound."
    
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.__breed = breed

    def GetBreed(self):
        return self.__breed

    def speak(self):
        return f"{self.GetName()} barks."

def main():
    generic_animal = Animal("Generic Animal", 5)
    print(generic_animal.speak())

    dog = Dog("Buddy", 2, "Golden Retriever")
    print(dog.speak())

    print(f"{dog.GetName()} is a {dog.GetBreed()} and is {dog.GetAge()} years old.")

if __name__ == "__main__":
    main()
