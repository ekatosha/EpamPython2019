"""
С помощью паттерна "Цепочка обязанностей" составьте список покупок для выпечки блинов.
Необходимо осмотреть холодильник и поочередно проверить, есть ли у нас необходимые ингридиенты:
    2 яйца
    300 грамм муки
    0.5 л молока
    100 грамм сахара
    10 мл подсолнечного масла
    120 грамм сливочного масла
В итоге мы должны получить список недостающих ингридиентов.
"""

from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):
    """
    Интерфейс Обработчика объявляет метод построения цепочки обработчиков. Он
    также объявляет метод для выполнения запроса.
    """

    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    """
    Поведение цепочки по умолчанию может быть реализовано внутри базового класса
    обработчика.
    """

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        # Возврат обработчика отсюда позволит связать обработчики простым
        # способом, вот так:
        # handler1.set_next(handler2).set_next(handler3)
        return handler

    @abstractmethod
    def handle(self, request: Any) -> Optional[str]:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


"""
Все Конкретные Обработчики либо обрабатывают запрос, либо передают его
следующему обработчику в цепочке.
"""

EGGS = 2
Flour = 300
Milk = 0.5
Sugar = 100
Oil = 10
Butter = 120


class Fridge:
    def __init__(self, eggs=0, flour=0, Milk=0, Sugar=0, Oil=0, Butter=0):
        self.eggs = eggs  # 0 - 100 %
        self.flour = flour  # 0 - 4
        self.milk = Milk  # 0 - 100 %
        self.sugar = Sugar
        self.oil = Oil
        self.butter = Butter  # True or False


class EggHandler(AbstractHandler):
    def handle(self, fridge):
        if fridge.eggs - EGGS < 0:
            Egg_to_add = EGGS - fridge.eggs
            print(f"Нужно купить {Egg_to_add} яиц")
        if self._next_handler:
            return self._next_handler.handle(fridge)


class FlourHandler(AbstractHandler):
    def handle(self, fridge):
        if fridge.flour - Flour < 0:
            flour_to_add = Flour - fridge.flour
            print(f"Нужно купить {flour_to_add} гр муки")
        if self._next_handler:
            return self._next_handler.handle(fridge)


class MilkHandler(AbstractHandler):
    def handle(self, fridge):
        if fridge.milk - Milk < 0:
            milk_to_add = Milk - fridge.milk
            print(f"Нужно купить {milk_to_add} л молока")
        if self._next_handler:
            return self._next_handler.handle(fridge)


class SugarHandler(AbstractHandler):
    def handle(self, fridge):
        if fridge.sugar - Sugar < 0:
            sugar_to_add = Sugar - fridge.sugar
            print(f"Нужно купить {sugar_to_add} гр сахара")
        if self._next_handler:
            return self._next_handler.handle(fridge)


class OilHandler(AbstractHandler):
    def handle(self, fridge):
        if fridge.oil - Oil < 0:
            oil_to_add = Oil - fridge.oil
            print(f"Нужно купить {oil_to_add} мл масла")
        if self._next_handler:
            return self._next_handler.handle(fridge)


class ButterHandler(AbstractHandler):
    def handle(self, fridge):
        if fridge.butter - Butter < 0:
            butter_to_add = Butter - fridge.butter
            print(f"Нужно купить {butter_to_add} гр сливочного масла")
        if self._next_handler:
            return self._next_handler.handle(fridge)


def shopping_list(fridge):
    egg_handler = EggHandler()
    flour_handler = FlourHandler()
    milk_handler = MilkHandler()
    sugar_handler = SugarHandler()
    oil_handler = OilHandler()
    butter_handler = ButterHandler()

    egg_handler.set_next(flour_handler).set_next(milk_handler).set_next(sugar_handler).set_next(oil_handler).set_next(
        butter_handler)

    egg_handler.handle(fridge)


fridge_to_check = Fridge(eggs=1, flour=200, Milk=1, Sugar=500, Oil=5, Butter=0)

shopping_list(fridge_to_check)