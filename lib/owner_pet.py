class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner = None):
        if pet_type not in self.PET_TYPES:
            raise Exception("Invalid pet type")
        
        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        Pet.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if isinstance(pet.owner, Owner) and pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Invalid pet type")
        pet.owner = self

    def get_sorted_pets(self):
        sorted_pets = sorted(self.pets(), key=lambda x: x.name)
        return sorted_pets