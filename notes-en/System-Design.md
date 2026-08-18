# System Design

### SOLID

SOLID is a set of five object-oriented design principles that help make code more maintainable, flexible, and easier to understand.
1. **S — Single Responsibility Principle**
    - A class should have only one reason to change 
    - Every class should have a single responsibility or single job or single purpose.
2. **O — Open/Closed Principle**
    - Classes should be open for extension but closed for modification. 
    - Add new behavior without changing existing code.
3. **L — Liskov Substitution Principle (!Important)** 
    - Derived or child classes must be able to replace their base or parent classes.
    - Ensures that any subclass can be used in place of its parent class without causing unexpected behavior in the program
4. **I — Interface Segregation Principle**
    - Don't force a class to implement interfaces it doesn't use. 
    - Prefer smaller, specific interfaces over one large one.
5. **D — Dependency Inversion Principle**
    - High-level modules shouldn't depend on low-level modules directly.
    - Depend on abstractions (interfaces), not concrete implementations. 