# Singleton Pattern

## Tips
1. The Singleton Pattern ensures a class has only one instance, and provides a global point of access to it.

## Summary
1. This pattern often used on sharing resource management, such as thread pool and database connection pool.
1. We can omit locking mechanism if this singleton object is not in multi-threading environment.