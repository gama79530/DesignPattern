# Facade Pattern
 
## Tips
1. The Facade Pattern provides a unifi ed interface to a set of interfaces in a subsytem. Facade defi nes a higherlevel interface that makes the subsystem easier to use.
1. Principle of Least Knowledge - talk only to your immediate friends. 

## Summary
1. We should only invoke methods that belong to :
   - The object itself
   - Objects passed in as a parameter to the method
   - Any object the method creates or instantiates
   - Any components of the object

