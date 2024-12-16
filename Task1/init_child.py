import random


class Child:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.feed_calm = random.choice(['спокоен', 'зол', 'встревожен', 'обеспокоен', 'расстроен'])
        self.feed_hungry = random.choice(['голоден', 'сыт'])


    def __str__(self):
        return (f'имя ребенка - {self.name}, возраст ребенка - {self.age}, ребенок - {self.feed_calm} и ребенок - {self.feed_hungry}')


    def __repr__(self):
        return(f'{self.name}, {self.age} лет/год(а)')
