# Command Pattern

## Tips
1. The Command Pattern encapsulates a request as an object, thereby letting you parameterize other objects with different requests, queue or log requests, and support undoable operations.
   - Invoker is responsible to invoke command which is encapsulated in command object.
   - Product objects encapsulate actual action for command objects.
   - Command is an API interface, all concrete command class should implement it and delegate reaction to product objects.
   - Client object is responsible to prepare command objects for invoker and send signal to invoker.

1. More uses of the Command Pattern
   - Queuing requests
   - Logging requests

## Summary
1. Role of programmer
   - Command objects and Product objects are provided by third party.
   - Invoker is contributed by library constructor.
   - Client object is created by library user.

1. Macro command
   - Macro command collect several command objects and execute them one-by-one.
   - We can control execution order by controlling command order.

1. We can save status snapshot in command objects and command invoking order in invoker to implement undo functionality.
