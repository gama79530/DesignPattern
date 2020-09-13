# Singleton Pattern (Creational, Object)

## Example description
1. We create ChocolateBoiler object that implement singleton Pattern.
1. We applies this pattern because we want to guarantee that ChocolateBoiler have stable manufacturing process on chocolate.

## Comment
1. This pattern is often used on sharing resource management, such as thread pool and database connection pool.
1. We can omit locking mechanism if this singleton object is not in multi-threading environment.
1. Implementation of singleton pattern depends on used programming language.

## Summary
1. **The Singleton Pattern** ensures a class has only one instance, and provides a global point of access to it.
