"""
    # All classes should extend Iterator and override the following or methods.
    def hasNext(self) :
    def next(self) :
    def remove(self) :
"""
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
            pass
        else:
            return False  
#   public boolean hasNext() {
#     if (stack.empty()) {
#       return false;
#     }
#     else {
#       Iterator iterator = (Iterator)stack.peek();
#       if (!iterator.hasNext()) {
#         stack.pop();
#         return hasNext();
#       }
#       else {
#         return true;
#       }
#     }
#   }
        
    def next(self) :
        if self.hasNext():
            iterator = self.stack[-1]
            menu_component = iterator.next()
#   public Object next() {
#     if (hasNext()) {
#       Iterator iterator = (Iterator)stack.peek();
#       MenuComponent menuComponent = (MenuComponent)iterator.next();
#       if (menuComponent instanceof Menu) {
#         stack.push(menuComponent.createIterator());
#       }
#       return menuComponent;
#     } else {
#         return null;
#     }
#   }

class NullIterator(Iterator):
    def next(self):
        return None

    def hasNext(self):
        return False