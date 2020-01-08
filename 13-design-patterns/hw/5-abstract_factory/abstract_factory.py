"""
Представьте, что вы пишите программу по формированию и выдачи комплексных обедов для сети столовых, которая стала
расширяться и теперь предлагает комплексные обеды для вегетарианцев, детей и любителей китайской кухни.
С помощью паттерна "Абстрактная фабрика" вам необходимо реализовать выдачу комплексного обеда, состоящего из трёх
позиций (первое, второе и напиток).
В файле menu.yml находится меню на каждый день, в котором указаны позиции и их принадлежность к
определенному типу блюд.
"""

from abc import ABC, abstractmethod
import yaml

with open('menu.yml', encoding='utf8') as file:
    menu = yaml.load(file)


class AbstractCourses(ABC):  # курс

    @abstractmethod
    def create_course(self, menu) -> str:
        pass


class FirstCourses:

    def create_course(self, menu) -> str:
        return menu['first_courses']


class SecondCourses(AbstractCourses):

    def create_course(self, menu) -> str:
        return menu['second_courses']


class Drinks(AbstractCourses):

    def create_course(self, menu) -> str:
        return menu['drinks']


class AbstractKitchen(ABC):

    @abstractmethod
    def create_dish(self, menu) -> None:
        pass


class СhildKitchen(AbstractKitchen):

    def create_dish(self, menu) -> str:  
        return menu['child']


class СhineseKitchen(AbstractKitchen):

    def create_dish(self, menu) -> str: 
        return menu['chinese']


class VeganKitchen(AbstractKitchen):

    def create_dish(self, menu) -> str: 
        return menu['vegan']


class AbstractFactory(ABC):
    """
    Интерфейс Абстрактной Фабрики объявляет набор методов, которые возвращают
    различные абстрактные продукты. Эти продукты называются семейством и связаны
    темой или концепцией высокого уровня. Продукты одного семейства обычно могут
    взаимодействовать между собой. Семейство продуктов может иметь несколько
    вариаций, но продукты одной вариации несовместимы с продуктами другой.
    """

    @abstractmethod
    def get_course(self) -> AbstractKitchen:  
        pass


class VeganFactory(AbstractFactory):

    def get_course(self):
        return VeganKitchen()


class ChineseFactory(AbstractFactory):

    def get_course(self):
        return СhineseKitchen()


class ChildFactory(AbstractFactory):

    def get_course(self):
        return СhildKitchen()


def client_code(factory: AbstractFactory, weekday, menu) -> None:
    """
    Клиентский код работает с фабриками и продуктами только через абстрактные
    типы: Абстрактная Фабрика и Абстрактный Продукт. Это позволяет передавать
    любой подкласс фабрики или продукта клиентскому коду, не нарушая его.
    """
    for key, value in menu.items():
        if key.lower() == weekday.lower():
            first = FirstCourses().create_course(menu[key])
            second = SecondCourses().create_course(menu[key])
            drinks = Drinks().create_course(menu[key])
            kitchen = factory.get_course()
            print('первое блюдо:', kitchen.create_dish(first))
            print('второе блюдо:', kitchen.create_dish(second))
            print('напиток:', kitchen.create_dish(drinks))


if __name__ == "__main__":
    """
    Клиентский код может работать с любым конкретным классом фабрики.
    """
    print("Клиент: Тестируем код клиента с фабрикой для веганов:")
    client_code(VeganFactory(), 'monday', menu)

    print("\n")

    print("Клиент: Тестируем код клиента с фабрикой для детей:")
    client_code(ChildFactory(), 'tuEsday', menu)
