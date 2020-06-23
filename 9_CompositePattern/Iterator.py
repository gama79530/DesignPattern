"""
    # All classes should extend Iterator and override the following or methods.
    def hasNext(self) :
    def next(self) :
    def remove(self) :
"""
import MenuComponent

class Iterator :
    def hasNext(self) :
        raise AttributeError()

    def next(self) :
        raise AttributeError()
    
    def remove(self) :
        raise AttributeError()

class CompositeIterator(Iterator):
    def __init__(self, iterator):
        self.stack = []
        self.stack.append(iterator)
        
    def hasNext(self) :
        if self.stack:
            iterator = self.stack[-1]
            if iterator.hasNext():
                return True
            else:
                self.stack.pop()
                return self.hasNext()
        else:
            return False  
        
    def next(self) :
        if self.hasNext():
            iterator = self.stack[-1]
            menu_component = iterator.next()
            if isinstance(menu_component, MenuComponent.Menu):
                self.stack.append(menu_component.createIterator())
        else:
            return None

class ListIterator(Iterator):
    def __init__(self, _list):
        self.position = 0
        self._list = _list
        
    def next(self):
        element = self._list[self.position]
        self.position += 1
        return element

    def hasNext(self):
        return self.position < len(self._list)

class NullIterator(Iterator):
    def next(self):
        return None

    def hasNext(self):
        return False