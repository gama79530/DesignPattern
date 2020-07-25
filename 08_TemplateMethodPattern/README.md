# Template Method Pattern (Behavioral, Class)

## Example description
1. We build a standard process to create caffeine beverages, but we need to provide a little flexibility about some intermediate steps so that we can create different caffeine beverages, such as coffee and tea.

## Comment
1. Analysis skill
   - Classifying tasks by whether used algorithm are similar.
   - For each class, verifying whether each algorithm step is common or flexible.
   - For each class, verifying whether each algorithm step is necessary or optional.

1. Design Trick
   - Encapsulating whole algorithm in a method of super class.
   - Encapsulating common steps in methods of super class as default.
   - Encapsulating flexible steps in abstract methods of super class and implement them in subclass.
   - Using hook when the step is optional.
   - Using composition to increasing flexibility.
   - Using callback function to increasing flexibility.

## Summary
1. **The Template Method** Pattern defines the skeleton of an algorithm in a method, deferring some steps to subclasses. Template Method lets subclasses redefine certain steps of an algorithm without changing the algorithm’s structure.