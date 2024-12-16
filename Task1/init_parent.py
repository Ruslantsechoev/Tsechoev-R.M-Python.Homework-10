import random


class Parent:

    _do_that_calm_child = ['поиграть в настольную игру',
                           'пособирать мазайку',
                           'обнять, Ведь обнимашки еще никому никогда не вредили!',
                           'поцеловать',
                           'подбодрить его, сказав, что все будет хорошо!',
                           'предложить поговорить ему, выслушать его']

    _eat_for_child = ['пюрешка с котлеткой',
                      'макарошки с балоньезе',
                      'пельмеши со сметанкой',
                      'плов по-узбекски',
                      'греча с гуляшом',
                      'пицца и бургеры',
                      'лазанья']


    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.children = list()


    def check_age_parent_with_child(self, other):
        '''Метод по проверке разницы в возрасте с ребенком и добавление ребенка в список детей'''
        if self.age - other.age < 16:
            print("Разница в возрасте между родителем и ребенком должна быть не менее 16 лет")
        else:
            self.children.append(other.__repr__())


    def parent_calm_children(self, other):
        '''Метод по успокоению ребенка, родитель выбирает, как успоить ребенка'''
        if other.feed_calm != 'спокоен':
            print(f'Ребенок - {other.name} {other.feed_calm}, {self.name} решает это исправить, '
                  f'поэтому выбирает - {random.choice(self._do_that_calm_child)}')

        else:
            print(f'Ребенок - {other.name} спокоен, ничего делать не нужно')


    def is_feed_child(self, other):
        '''Метод по проверке голоден ли ребенок или нет, если голоден, то родитель выбирает чем его накормить'''

        if other.feed_hungry == 'голоден':
            print(f'Ребенок - {other.name} {other.feed_hungry}, {self.name} решает покормить его, '
                  f'поэтому выбирает - {random.choice(self._eat_for_child)}  ')



    def information_to_children(self):
        '''Метод по отображению всех детей у родителя'''
        count = 0

        if len(self.children) == 0:
            count = 0
        else:
            for _ in range(len(self.children)):
                count += 1

        print(f'У родителя - {self.name}, {count} детей: {self.children}')




    def __str__(self):
        '''Метод по красивуму отображению информации о родителе'''
        return (f'имя родителя - {self.name}, возраст - {self.age} и дети - {self.children}')


