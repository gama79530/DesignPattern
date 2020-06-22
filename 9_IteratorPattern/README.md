# Iterator Pattern

## Tips
1. The Iterator Pattern provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation.

1. A class should have only one reason to change.

1. Internal iterators v.s. external iterator
   - External iterator which means that the client controls the iteration by calling next() to get the next element.
   - An internal iterator is controlled by the iterator itself.
   - External iterators are more flexible.
   - Internal iterators are easier to use.
   
## Summary
1. Separating reason to change relies on experience.