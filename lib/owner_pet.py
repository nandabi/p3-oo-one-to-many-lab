class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all_pets = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        if pet_type.lower() not in self.PET_TYPES:
            raise ValueError(f"Invalid pet type '{pet_type}'. Must be one of: {', '.join(self.PET_TYPES)}")
        self.pet_type = pet_type.lower()
        if owner is not None:
            if not isinstance(owner, Owner):
                raise TypeError("Owner must be an instance of the Owner class.")
        self.owner = owner
        self.all_pets.append(self)

class Owner:
    def __init__(self, name):
        self.name = name
        self.pet_list = []


    def get_pets(self):
        owner_pets = []
        for pet in Pet.all_pets:
            if pet.owner == self:
            owner_pets.append(pet)
            return owner_pets        

    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self 
            self.pet_list.append(pet)
        else:
            raise TypeError("Only instances of the Pet class can be added as pets.")

    def get_sorted_pets(self):
        sorted_pets = sorted(self.pets, key=lambda pet: pet.name)
        return sorted_pets              
        
        