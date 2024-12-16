from init_animal import Animal

class Fish(Animal):

    def __init__(self, name: str, max_depth: float):
        super().__init__(name=name)
        self.max_depth = max_depth


    def speak(self):
        return ("pow-pow")


    def _depth(self):
        '''Метод по определению типа рыбы в зависимоти от глубины'''
        if self.max_depth < 10:
            return 'Мелководная рыба'
        elif self.max_depth > 100:
            return 'Глубоководная рыба'
        else:
            return 'Средневодная рыба'


    def __str__(self):
        return (f'Рыба - {self.name}, относится к типу - {self._depth()}, максимальная глубина - {self.max_depth}')