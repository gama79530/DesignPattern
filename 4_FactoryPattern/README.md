# Factory Pattern

## Tips
1. Depending upon abstractions. Do not depend upon concrete classes.

## Summary
1. Simple factory is an easy trick to try to separating the possible change of object instantiation.
   - Change of object instantiation is due to instancing object conditionally.
   - One kind of changing is that maybe we want to add additional types of object or delete existing types of object.

1. The Factory Method Pattern defines an interface
for creating an object, but lets subclasses decide which class to instantiate. Factory Method lets a class defer instantiation to subclasses.
   - Factory method create concrete object which implement a certain interface.
   - Subclass decide which concrete object will be instanced.
   - Superclass decide how to use the object which is created by the factory method.

1. The Abstract Factory Pattern provides an interface
for creating families of related or dependent objects
without specifying their concrete classes.
   - Abstracting product, client and factory
   - Client object uses Factory object to instance product object and decide how to use it.
   - Product objects are composition objects.
   - Factory object decides how to composite product object.

1. Trying to composite product object and use Abstract Factory Pattern if the types of product object is very much. Otherwise, using Factory Method Pattern is easier.