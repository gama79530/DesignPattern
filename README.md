# Design Pattern
 
## Description
1. All scenarios and designs in this project are from the book [Head First Design Patterns](https://www.oreilly.com/library/view/head-first-design/0596007124/).  
1. This project is Python version implementation.

## Comment
1. As time passing, the problem may not be the same as the original.
1. Only using a certain pattern when current problem is similar to pattern's context. 
1. Using pattern for reusability and more clear structure.

## Design Principle
1. Keep it simple.
1. Take out what you don’t really need.
1. Identify the aspects of your application that vary and separate them from what stays the same.
1. Program to an interface, not an implementation.
1. Favor composition over inheritance.

## Summary
### What is pattern
1. A _Pattern_ is a **solution** to a **problem** in a **context**.
   - The _context_ is the situation in which the pattern applies. This should be a **recurring** situation.
   - The _problem_ refers to the **goal** you are trying to achieve in this context, but it also refers to any **constraints** that occur in the context.
   - The _solution_ is what you're after: a general design that **anyone can apply** which resolves the goal and set of constraints.

### How to describe design pattern
1. **Pattern name**
1. The **intent** describes what the pattern does in a short statement. You can also think of this as the pattern’s definition.
1. The **motivation** gives you a concrete
scenario that describes the problem and
how the solution solves the problem.
1. The **applicability** describes situations
in which the pattern can be applied.
1. The **structure** provides a diagram illustrating the relationships among the classes that participate
in the pattern.
1. The **participants** are the classes and
objects in the design. This section describes their responsibilities and roles in the pattern.
1. **Collaborations** tells us how the participants work together in the pattern.
1. The **consequences** describe the effects that using this pattern may have: good and bad.
1. **Implementation / Sample code**
1. **Known uses** describes examples of this pattern
found in real systems.
1. **Related patterns** describes the relationship between this pattern and others.

### Ways to classification
1. Based on their purposes
   - **Creational** patterns involve object instantiation and all provide a way to decouple a client from the objects it needs to instantiate.
   - **Behavioral** Patterns are concerned with how classes and objects interact and distribute responsibility.
   - **Structural** patterns let you compose classes or objects into larger structures.

1. Classified by whether or not the pattern deals with classes or objects
   - **Class** patterns describe how relationships between classes are defined via inheritance. Relationships in class patterns are established at compile time.
   - **Object** patterns describe relationships between objects and are primarily defined by composition. Relationships in object patterns are typically created at runtime and are more dynamic and flexible.