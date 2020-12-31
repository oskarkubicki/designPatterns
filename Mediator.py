from __future__ import annotations
from abc import ABC


class Mediator(ABC):

    def notify(self, sender: object, event: str) -> None:
        pass


class CalculatorMediator(Mediator):
    def __init__(self, component1: AdditionComponent, component2: MultiplicationComponent) -> None:
        self._component1 = component1
        self._component1.mediator = self
        self._component2 = component2
        self._component2.mediator = self

    def notify(self, sender: object, event: str, number: int,counter:int) -> None:
        if counter <=1 and event == "addition" :
            self._component2.multiplication(number)
        elif counter <=1 and event == "multiplication" and counter:
            self._component1.addition(number)


class BaseComponent:

    def __init__(self, mediator: Mediator = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator


class AdditionComponent(BaseComponent):

    def addition(self, number1: int):
        counter= 0
        number3 = number1 + number1
        print(number3)
        self.mediator.notify(self, 'addition', number3,counter)
        counter += 1


class MultiplicationComponent(BaseComponent):

    def multiplication(self, number1: int):
        counter= 0
        number3 = number1 * number1
        print(number3)
        self.mediator.notify(self, 'multiplication', number3,counter)
        counter += 1


multiplication = MultiplicationComponent()
addition = AdditionComponent()
mediator = CalculatorMediator(addition, multiplication)
print(addition.addition(5))
