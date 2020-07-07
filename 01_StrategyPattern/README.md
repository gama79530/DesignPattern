# Strategy Pattern (Behavioral, Object)

## Example description
1. We want to create a duck objects family. 
1. Each kind of duck has a common behaviors, _swim_.
1. Each kind of duck has 3 behaviors, _quack_,  _fly_ and _display_, which may perform differently.

## Comment
1. Find interchangeable part by experience.
1. We can encapsulate algorithm in a class and use delegation to perform behavior if the programming language does not support callable attribute.

## Summary
1. **The Strategy Pattern** defines a family of algorithms, encapsulates each one, and makes them interchangeable. Strategy lets the algorithm vary independently from clients that use it.
