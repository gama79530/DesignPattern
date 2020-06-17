# Template Method Pattern

## Tips
1. The Template Method Pattern defines the skeleton of an algorithm in a method, deferring some steps to subclasses. Template Method lets subclasses redefine certain steps of an algorithm without changing the algorithm’s structure.
1. Low-level components don’t call high-level components.

## Summary
1. Designing
   - Classify tasks on the bases of similar algorithm.
   - For each class of task, verifying whether each algorithm step is common or flexible.
   - For each class of task, verifying whether each algorithm step is necessary or optional.

1. Tricks
   - common step : implement by super class
   - flexible step : abstract in super class and implement by subclass
   - optional step : use hook.