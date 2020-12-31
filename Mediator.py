from __future__ import annotations
from abc import ABC


class Mediator(ABC):


    def notify(self, sender: object, event: str) -> None:
        pass


class ConcreteMediator(Mediator):
    def __init__(self, component1: Component1, component2: Component2) -> None:
        self._component1 = component1
        self._component1.mediator = self
        self._component2 = component2
        self._component2.mediator = self

    def notify(self, sender: object, event: str) -> None:
        if event == "adddition":
            print("Mediator reacts on A and triggers following operations:")
            self._component2.do_c()
        elif event == "subtraction":
            print("Mediator reacts on D and triggers following operations:")
            self._component1.do_b()
            self._component2.do_c()


class BaseComponent:
    """
    The Base Component provides the basic functionality of storing a mediator's
    instance inside component objects.
    """

    def __init__(self, mediator: Mediator = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator

class AdditionComponent(BaseComponent):

    def addition(self,number1:int,number2:int):

        number3=number1+number2
        self._mediator.notify()



class MultiplicationComponent(BaseComponent):

    def addition(self,number1:int,number2:int):

        number3 = number1*number2
        self._mediator.notify()

