"""
Используя паттерн "Декоратор" реализуйте возможность дополнительно добавлять к кофе
    маршмеллоу, взбитые сливки и сироп, а затем вычислить итоговую стоимость напитка.
"""

from abc import ABC, abstractmethod


class Component:
    def get_cost(self):
        raise NotImplementedError("Override get_cost method")

    def get_ingredients(self):
        pass

    def get_tax(self):
        return 0.1 * self.get_cost()


class BaseCoffe(Component):

    def get_cost(self):
        return 90

    def get_ingredients(self):
        return 'coffee'


class AbstractCoffeeDecorator(Component):
    """
    Базовый класс Декоратора следует тому же интерфейсу, что и другие
    компоненты. Основная цель этого класса - определить интерфейс обёртки для
    всех конкретных декораторов. Реализация кода обёртки по умолчанию может
    включать в себя поле для хранения завёрнутого компонента и средства его
    инициализации.
    """

    def __init__(self, decorated_coffee):
        self.decorated_coffee = decorated_coffee

    def get_cost(self):
        return self.decorated_coffee.get_cost()

    def get_ingredients(self):
        return self.decorated_coffee.get_ingredients()


class Whip(AbstractCoffeeDecorator):
    """
    Конкретные Декораторы вызывают обёрнутый объект и изменяют его результат
    некоторым образом.
    """

    def __init__(self, decorated_coffee):
        super(Whip, self).__init__(decorated_coffee)

    def get_cost(self):
        return self.decorated_coffee.get_cost() + 1

    def get_ingredients(self):
        return self.decorated_coffee.get_ingredients() + ', Whip'


class Marshmallow(AbstractCoffeeDecorator):
    def __init__(self, decorated_coffee):
        super(Marshmallow, self).__init__(decorated_coffee)

    def get_cost(self):
        return self.decorated_coffee.get_cost() + 5

    def get_ingredients(self):
        return self.decorated_coffee.get_ingredients() + ', Marshmallow'


class Syrup(AbstractCoffeeDecorator):
    def __init__(self, decorated_coffee):
        super(Syrup, self).__init__(decorated_coffee)

    def get_cost(self):
        return self.decorated_coffee.get_cost() + 0.25

    def get_ingredients(self):
        return self.decorated_coffee.get_ingredients() + ', Syrup'


if __name__ == "__main__":
    coffe = BaseCoffe()
    coffe = Whip(coffe)
    coffe = Marshmallow(coffe)
    coffe = Syrup(coffe)
    print("Итоговая стоимость за кофе: {}".format(str(coffe.get_cost())))