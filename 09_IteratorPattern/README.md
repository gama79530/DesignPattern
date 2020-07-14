# Iterator Pattern (Behavioral, Object)

## Example description
1. We want to make an **Waitress** object which is used to integrate 3 **Menus** object which come from different restaurant so that we can print all information in these 3 **Menu** objects.
1. Each **Menus** object aggregates lots of **MenuItem** object and is an Iterable object.
1. **MenuItem** object has _name_, _description_, _vegetarian_ and _price_ attributes.

## Comment
1. Python have 2 ways to define an [_Iterable_](https://docs.python.org/3/glossary.html#term-iterable) class
   - Implement _\_\_iter(self)\_\__ method which returns an _Iterator_ object.
   - Implement _\_\_getitem(self, key)\_\__ and _\_\_len(self)\_\__ methods so that this object is also a [_Sequence_](https://docs.python.org/3/glossary.html#term-sequence) class.

1. Python have 1 way to define an [_Iterator_](https://docs.python.org/3/glossary.html#term-iterator) class
   - Implement _\_\_next(self)\_\__ method which returns the next iterated object.

1. 2 classes of iterator
   - An **external** iterator is that the client controls the iteration by calling _next()_ to get the next element.
   - An **internal** iterator is controlled by the iterator itself, so you need a way to pass an operation to an iterator.
   - Internal iterators are less flexible but they are easier to use.
   - Python use _for-loop_ to implement **external** iterator mechanism and use a _map_ function to **internal** iterator mechanism.

## Summary
1. **The Iterator Pattern** provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation.