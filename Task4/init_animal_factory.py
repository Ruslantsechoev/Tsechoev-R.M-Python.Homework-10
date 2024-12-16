import random
from init_bird import Bird
from init_fish import Fish
from init_mammal import Mammal
from init_animal import Animal

class AnimalFactory:

    def create_animal(self):
        '''Первый способ получения типа'''
        bird = Bird(name="Синичка", wingspan=self._random_num_for_bird(), wing_len=self._random_num_for_bird()).__str__()
        fish = Fish(name='Окунь', max_depth=self._random_num_for_fish()).__str__()
        mammal = Mammal(name="Волк", weight=self._random_num_for_mammal()).__str__()
        self.factory = [bird, fish, mammal]


    def create_animal2(animal_type: str, *args) -> Animal:
        '''Второй способ получения типа животных'''
        animal_classes = {
            'Bird': Bird,
            'Fish': Fish,
            'Mammal': Mammal
        }

        if animal_type in animal_classes:
            return animal_classes[animal_type](*args)
        else:
            raise ValueError(f'Unknown animal type: {animal_type}')



    def __str__(self):
        return (self.factory)


    def _random_num_for_bird(self) -> float:
        return random.uniform(0.1, 1.0)

    def _random_num_for_mammal(self) -> float:
        return random.uniform(15.0, 90.0)

    def _random_num_for_fish(self) -> float:
        return random.uniform(1.0, 200.0)



if __name__ == '__main__':
    factory = AnimalFactory()
    factory.create_animal()
    print(factory.__str__())

    bird = AnimalFactory.create_animal2('Bird', 'Синичка', random.uniform(0.1, 1.0), random.uniform(0.1, 1.0))
    fish = AnimalFactory.create_animal2('Fish', "Окунь", random.uniform(1.0, 200.0))
    mammal = AnimalFactory.create_animal2('Mammal', 'Волк',  random.uniform(15.0, 90.0))

    print(bird)
    print(fish)
    print(mammal)
