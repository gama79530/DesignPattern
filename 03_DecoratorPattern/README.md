# Decorator Pattern (Structural, Object)

## Example description
1. We want to build a system to represent _Beverage_ objects. 
   - Each _Beverage_ objects can show its description and price.
   - In our system, we can add some optional _Condiment_ into given _Beverage_ object.

## Comment
1. The desired object is consisted by a base objects and uncertain number of plug-in objects.
1. 3 part consisting this pattern
   - General interface
   - Base object : perform basic method behavior.
   - Plug-in object : base on basic method behavior, adding some optional behavior on it.

1. Base object is like source and plug-in object is like pipe.
1. This pattern let us easy to add new base object and plug-in object.

## Summary
1. **The Decorator Pattern** attaches additional responsibilities to an object dynamically. Decorators provide a flexible alternative to subclassing for extending functionality.
