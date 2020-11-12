class farm:

    __name = ""
    __money = 1000
    __animals = []
    __farmers = []
    __crops = []

    def __init__(self, name):
        self.name = name

    def add_new_animal(self):
        animal_name = input("What is the animal's name?:\n")
        animal_species = input("What is the animal's species?:\n")
        self.__animals.append(animals(animal_name, animal_species))

    def list_animals(self):
        for x in range(len(self.__animals)):
            self.__animals[x].return_name()

    def employ_new_farmer(self):
        farmer_name = input("What is the new farmer's name?:\n")
        farmer_energy = int(
            input("What is the new farmer's max energy level?:\n"))
        farmer_current = farmer_energy
        farmer_wages = int(input("How much does this new farmer cost?:\n"))
        self.__farmers.append(
            farmers(farmer_current, farmer_energy, farmer_wages, farmer_name))

    def pay_farmers(self):
        pass

    def list_farmers(self):
        for x in range(len(self.__farmers)):
            self.__farmers[x].return_name()

    def save(self):
        empty_file = open("save.txt", "w")
        empty_file.write("")
        empty_file.close()
        save_file = open("save.txt", "a")
        for x in range(len(self.__animals)):
            save_file.write(self.__animals[x].return_name() + "," +
                            self.__animals[x].return_species() + "\n")

    def load(self):
        load_file = open("save.txt", "r")
        for line in load_file:
            animal = line.split(",")
            animal_name = animal[0]
            animal_species = animal[1]
            self.__animals.append(animals(animal_name, animal_species))


class animals:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        #self.weight = weight

    def return_name(self):
        print(self.name)

    def return_species(self):
        print(self.species)


class crops:
    pass


class farmers:
    def __init__(self, current_energy, max_energy, wages, name):
        self.current_energy = current_energy
        self.max_energy = max_energy
        self.wages = wages
        self.name = name

    def return_name(self):
        print(self.name)

    def return_wages(self):
        print(self.wages)

    def set_wages(self):
        new_wages = int(input("What is the new salary for this farmer?:\n"))
        self.wages = new_wages

    def return_energy_level(self):
        print(self.energy)

    def complete_task(self):
        energy_used = int(input("How much energy has been used?:\n"))
        self.energy = self.energy - energy_used

    def recover_energy(self):
        pass


class farmdog(animals):
	def __init__(self):
		super.__init__()
		self.noise = "Woof"

	def bark(self):
		print(self.noise)


farm1 = farm("Old McDonald's Farm")
farm1.load()
farm1.add_new_animal()
#farm1.employ_farmers()
#farm1.list_farmers()
farm1.list_animals()
farm1.save()
