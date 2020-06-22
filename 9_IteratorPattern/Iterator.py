"""
    # All classes should extend Iterator and override the following or methods.
    def hasNext(self) :
    def next(self) :
    def remove(self) :
"""
class Iterator :
    def hasNext(self) :
        assert False, 'This method should be overrided.' 

    def next(self) :
        assert False, 'This method should be overrided.' 
    
    def remove(self) :
        assert False, 'This method should be overrided.' 

class CafeMenuIterator(Iterator):
    def __init__(self, items):
        self.position = 0
        self.items = items
        self.keys = list(self.items.keys())

    def hasNext(self) :
        return self.position < len(self.items)

    def next(self) :
        menu_item = self.items[self.keys[self.position]]
        self.position += 1
        return menu_item

    def remove(self) :
        if self.position <= 0:
            raise ValueError("You can't remove an item until you've one at least one next()")
        del self.items[self.keys[self.position]]
        del self.keys[self.position]

class DinerMenuIterator(Iterator):
    def __init__(self, items):
        self.position = 0
        self.items = items

    def hasNext(self) :
        return self.position < len(self.items)

    def next(self) :
        menu_item = self.items[self.position]
        self.position += 1
        return menu_item

    def remove(self) :
        if self.position <= 0:
            raise ValueError("You can't remove an item until you've one at least one next()")
        del self.items[self.position]

class PancakeHouseMenuIterator(Iterator):
    def __init__(self, items):
        self.position = 0
        self.items = items

    def hasNext(self) :
        return self.position < len(self.items)

    def next(self) :
        menu_item = self.items[self.position]
        self.position += 1
        return menu_item

    def remove(self) :
        if self.position <= 0:
            raise ValueError("You can't remove an item until you've one at least one next()")
        del self.items[self.position]