class Dog:
    approved_breeds = ["Labrador", "Poodle", "German Shepherd", "Bulldog", "Beagle", "Golden Retriever"]

    def __init__(self, name="Buddy", breed="Labrador"):
        self.name = name  # Calls the setter
        self.breed = breed  # Calls the setter

    # Name property
    def get_name(self):
        print("Retrieving name.")
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            print(f"Setting name to {name}.")
            self._name = name
        else:
            print("Name must be a string between 1 and 25 characters.")

    name = property(get_name, set_name)

    # Breed property
    def get_breed(self):
        print("Retrieving breed.")
        return self._breed

    def set_breed(self, breed):
        if breed in Dog.approved_breeds:
            print(f"Setting breed to {breed}.")
            self._breed = breed
        else:
            print("Breed must be in the list of approved breeds.")

    breed = property(get_breed, set_breed)

# Example usage
dog1 = Dog(name="Max", breed="Poodle")
