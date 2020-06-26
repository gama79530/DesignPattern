# State Pattern

## Tips
1. The State Pattern allows an object to alter its behavior when its internal state changes. The object will appear to change its class.

1. Decision on the flow of state transitions
   - **In Context :**  appropriate when the state transitions are fixed. 
   - **In Concrete state :**  appropriate when the transitions are more dynamic
   - The disadvantage of having state transitions in the state classes is that we create dependencies between the state classes.
   -  Decision on the flow of state transitions affect which classes are closed for modification.

## Summary
1. This pattern is like a kind of programming skill, so designing a state machine diagram at first.
1. This pattern is powerful when the system changes make additional states but no additional actions.