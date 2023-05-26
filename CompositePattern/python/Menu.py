import abc
from typing import *

class MenuItem(metaclass=abc.ABCMeta):
    def __init__(self, description:str) -> None:
        self._description:str = description

    @abc.abstractmethod
    def __str__(self) -> str:
        return NotImplemented
    

class Menu(MenuItem):
    def __init__(self, description:str) -> None:
        super().__init__(description)
        self._components:List[MenuItem] = list()

    def addMenuItem(self, menuItem:MenuItem):
        self._components.append(menuItem)
    
    def removeMenuItem(self, menuItem:MenuItem) -> bool:
        try:
            self._components.remove(menuItem)
            return True
        except ValueError:
            return False
    

class MenuBook(Menu):
    def __init__(self, description:str) -> None:
        super().__init__(description)

    def __str__(self) -> str:
        output = f"======    {self._description}    ======\n"
        for component in self._components:
            output += f"{str(component)}\n"

        return output
    

class SubMenu(Menu):
    def __init__(self, description:str) -> None:
        super().__init__(description)

    def __str__(self) -> str:
        output = f"SubMenu {self._description}:\n"
        for component in self._components:
            if isinstance(component, Item):
                output += f"\t{str(component)}\n"
            else:
                temp = str(component).replace('\n', '\n\t')
                output += f"\n\t{temp}"

        return output
    

class Item(MenuItem):
    def __init__(self, description:str) -> None:
        super().__init__(description)

    def __str__(self) -> str:
        return self._description
    

