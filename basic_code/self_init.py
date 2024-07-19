# advantage
    # reusing code blocks
    # out initializing process helps here 
        # assigning objects to variables

# creating a basic class 
class computer_build:
    def __init__(self, name, RAM, SSD, value):
        self.name = name
        self.RAM = RAM
        self.SSD = SSD
        self.value = value 

        print('Variables are defined.')  

    def info_computer_specs(self):
        print(f'The {self.name} has {self.RAM} GB RAM, {self.SSD} GB SSD and a value of {self.value} euros.')

# using the basic class as foundation 
computer_1 = computer_build('macbook', 16 , 200, 1300)
computer_1.info_computer_specs()








