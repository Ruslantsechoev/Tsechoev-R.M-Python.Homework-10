from init_animal import Animal

class Mammal(Animal):

    def __init__(self, name: str, weight: float):
        super().__init__(name=name)
        self.weight = weight


    def speak(self):
        return 'вуф-вуф'


    def _category(self):
        '''Метод по определениб типа млекопитающего в зависимости от веса'''
        if self.weight < 1:
            return 'Малявка'
        elif self.weight > 200:
            return 'Гигант'
        else:
            return 'Обычный'


    def __str__(self):
        return (f'Млекопитающее - {self.name}, относится к типу - {self._category()}, вес - {self.weight}')