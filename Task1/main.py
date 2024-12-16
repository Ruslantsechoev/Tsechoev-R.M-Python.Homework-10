from init_child import Child
from init_parent import Parent


class Main:

    def __init__(self):
        parent1 = Parent(name='Kris', age=30)

        child1 = Child(name='Mila', age=10)
        child2 = Child(name='Bob', age=13)
        print(child1)
        print(child2)

        parent1.check_age_parent_with_child(child1)
        parent1.check_age_parent_with_child(child2)
        print(parent1)

        parent1.information_to_children()

        parent1.parent_calm_children(child1)
        parent1.parent_calm_children(child2)

        parent1.is_feed_child(child1)
        parent1.is_feed_child(child2)


if __name__ == '__main__':
    main = Main()
