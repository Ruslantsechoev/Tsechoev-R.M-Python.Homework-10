from init_animal import Animal

class Bird(Animal):

    def __init__(self, name: str, wingspan: float, wing_len: float):
        super().__init__(name=name)
        self.wingspan = wingspan
        self.wing_len = wing_len


    def speak(self):
        return "чик-чирик"

    def __str__(self):
        return (f'Птичка - {self.name}, размах крыла - {self.wingspan}, длина крыла - {self.wing_len}')