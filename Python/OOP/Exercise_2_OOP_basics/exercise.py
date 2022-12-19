####################################### OOP IN PYTHON ######################################
##################################### ENCAPSULATION ########################################
###################################### INHERITENCE #########################################

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_species(self):
        print('I am an animal. I can either be a wild animal or a pet animal.')

    def walk(self):
        return 'This animal can walk.'

    def attack(self):
        print("Some animals can attack! But only wild animals can because they have fangs and sharp teeth!")

    def __str__(self):
        return f"I am {self.name} and I am {self.age} years old."


class PetAnimal(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, age)
        self.species = species

    def show_species(self):
        super().show_species()
        return f"In this case I am {self.species}. \n"

    def attack(self):
        super().attack()
        return 'But this one is a pet. It can\'t attack. \n'


class WildAnimal(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, age)
        self.species = species

    def show_species(self):
        super().show_species()
        return f"In this case I am {self.species}. \n"

    def attack(self):
        super().attack()
        return 'This is a wild animal! Beware! It can attack because of the sharp teeth and claws!. \n'


pet1 = PetAnimal('Tommy', 2, 'Abyssinian Cat')
wild_animal1 = WildAnimal('Wolfie', 8, 'Grey Wolf')

print(pet1)
print(wild_animal1)

print(pet1.show_species())
print(wild_animal1.show_species())

print(pet1.attack())
print(wild_animal1.attack())
