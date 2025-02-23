class Pet:

    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []

    def __init__(self, name, pet_type, owner=""):
        self.name = name
        if pet_type in Pet.PET_TYPES:
            self.pet_type = pet_type
        else:
            raise Exception
        self.owner = owner
        Pet.add_pet_to_all(self)

    @classmethod
    def add_pet_to_all(cls, pet):
        cls.all.append(pet)

class Owner:

    def __init__(self, name):
        self.name = name
    
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception
    
    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
