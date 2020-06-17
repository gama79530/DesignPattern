# Template Method Pattern

## Tips
1. The Template Method Pattern defines the skeleton of an algorithm in a method, deferring some steps to subclasses. Template Method lets subclasses redefine certain steps of an algorithm without changing the algorithm’s structure.
1. Low-level components don’t call high-level components.

## Summary
1. Analysis skill
   - Classifying tasks by whether used algorithm are similar.
   - For each class, verifying whether each algorithm step is common or flexible.
   - For each class, verifying whether each algorithm step is necessary or optional.

1. Design Trick
   - Encapsulating whole algorithm in a method of super class.
   - Encapsulating common steps in methods of super class.
   - Encapsulating flexible steps in abstract methods of super class and implement them in subclass.
   - Using hook when the step is optional.
   - Using composition to increasing flexibility.
   - Using callback function to increasing flexibility.