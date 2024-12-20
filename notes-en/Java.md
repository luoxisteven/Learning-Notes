# Java

Key concepts:
   - **Object-Oriented Programming (OOP)**
   - **Three main features of Java (Encapsulation, Inheritance, Polymorphism)**
   - **Modifiers (default, public, private, protected)**
   - **Keywords (abstract, static, synchronized, transient, volatile)**
   - **Package packaging**

## Three main features of Java 
1. **Encapsulation**
2. **Inheritance**
3. **Polymorphism**

### Encapsulation
   - Hides the internal implementation details of an object and exposes only necessary interfaces.
   - Achieved through access modifiers such as `private`, `public`, `protected`.

### Polymorphism
   Achieved through `Overloading` and `Overriding`.
   1) `Override`:
      - Subclass re-implements a method from the parent class that is accessible, without changing the return type and parameters.
   2) `Overload`:
      - Same method name in the same class but with different parameters. The return type can be the same or different.

### Inheritance
   - A subclass can inherit properties and methods from a parent class, reusing its functionality and extending or overriding methods.
   - `extends`: Inherits properties and methods from the parent class.
      - Rule 1: Java supports single inheritance, i.e., a class can only extend one parent class.
      - Rule 2: Inherited classes do not inherit constructors.
      - Rule 3: The subclass can use `super()` to call the parent class constructor.
      - Rule 4: Sub-subclasses can access parent interfaces (supports multiple inheritance through interfaces, not classes).

## Implements Interface
   - An interface defines "what" a class can do, not "how" it does it, and is used to describe the capabilities of a class, not implementation details.
   - Unlike `extends`, a class can `implements` multiple interfaces.
   - An interface cannot be instantiated.
```java
interface Animal {
    public void eat();
    public void travel();
}
public class MammalInt implements Animal{
    public void eat(){
        System.out.println("Mammal eats");
    }
    public void travel(){
        System.out.println("Mammal travels");
    } 
}
```

## Data Types
- 1 Byte = 8 bits
- short: 2 Bytes
- int: 4 Bytes
- long: 8 Bytes
- float: 4 Bytes
- double: 8 Bytes
- boolean: 1 bit
- char: 2 Bytes

## Modifiers
- **Default**: Default class (no modifier), accessible within the same package, not accessible across packages.
- **Public**: Accessible across packages.
- **Private**: Only accessible within the class, not accessible from other classes even in the same package.
- **Protected**: Similar to default but can be accessed via inheritance outside the package.
    ```java
    package otherpackage;

    import mypackage.ParentClass;

    public class ChildClass extends ParentClass {
    public void accessProtectedMember() {
        System.out.println(protectedField); // Access protected field in subclass
        protectedMethod(); // Access protected method in subclass
    }
    }
    ```
## Package Packaging
Classes are packaged into a package like `com.example.myapp`. Classes within the same package can reference each other. When importing, you can import a specific class like `import java.util.ArrayList`; or the entire package like `import java.util.*`;, though the latter is not recommended.
-  If you have classes with the same name, use the fully qualified name to differentiate them:
    ```java
    import java.util.Date; // Import java.util.Date class

    public class DateExample {
        public static void main(String[] args) {
            // Using java.util.Date class
            Date utilDate = new Date();
            System.out.println("java.util.Date: " + utilDate);

            // Using fully qualified name for java.sql.Date class
            java.sql.Date sqlDate = new java.sql.Date(System.currentTimeMillis());
            System.out.println("java.sql.Date: " + sqlDate);
        }
    }
    ```

## Keywords
- **abstract**: Defines an abstract class that can be extended.
    ```java
    public abstract class Animal {
        // Abstract method without body
        public abstract void makeSound();

        // Concrete method with body
        public void sleep() {
            System.out.println("Sleeping...");
        }
    }
    public class Dog extends Animal {}
    ```
- **static**:
    ```java
    // 1) Static variable: Shared by all instances of the class.
    public class MyClass {
        static int staticCounter2 = 0; // Shared static variable
    }

    // 2) Static method: Can be called without creating an instance.
    public class Utility {
        public static int add(int a, int b) {
            return a + b;
        }
    }
    int result = Utility.add(5, 3);

    // 3) Static block: Executes once when the class is loaded.
    public class MyClass {
        static int staticVar;
        static {
            staticVar = 10; // Static block used for initialization
            System.out.println("Static block executed!");
        }
    }

    // 4) Static inner class: Can be created independently of the outer class instance.
    public class OuterClass {
        static class InnerClass {
            public void display() {
                    System.out.println("Static inner class method called!");
            }
        }
    }
    OuterClass.InnerClass inner = new OuterClass.InnerClass();
    inner.display();
    ```
- **synchronized**: Used to lock a method or block at the object level, allowing only one thread at a time to access the synchronized method.
    - Different instances do not interfere with each other’s synchronized methods.
- **transient**: Used during serialization to exclude a variable from being persisted.
    ```java
    private transient String password;
    ```
- **volatile**: Ensures that when a thread modifies a `volatile` variable, other threads can immediately see the updated value.


## Comments
```java
// This is a single-line comment

/*
This is a multi-line comment
Used to comment multiple lines of code
*/
int y = 20; // Initializing variable y to 20

/**
 * This is a documentation comment example
 * It typically contains detailed information about classes, methods, or fields
 */
public class MyClass {
    // Class members and methods
}
```

## Code Blocks
- Code blocks are sections of code wrapped in `{ }`.
    1. **Normal code block**: Regular code enclosed in `{ }`.
    2. **Static block**: Executes once when the class is loaded. Typically used for static variable initialization.
    ```java
    public class MyClass {
    static int staticCounter;
    static {
        staticCounter = 1;
        System.out.println("Static block executed.");
    }
    }
    MyClass myClass = new MyClass();
    ```
    3. **Instance initialization block**: Runs before constructors, executed every time an object is created.
    ```java
    public class MyClass {
        {
            System.out.println("Instance block executed.");
        }
    }
    ```
    4. **Synchronized block**: Used in multi-threading to allow only one thread to execute a portion of code at a time.
    ```java
    public void syncMethod() {
        synchronized (this) {
            // Code inside synchronized block
        }
    }
    ```

## Array
```java
dataType[] arrayRefVar;
arrayRefVar.length;  // Get array length
string.length();  // Get string length, note difference from array
Array.sort();
Array.equals();
```

## String
```java
Length: string.length();
Retrieve: string.charAt(int i); // Key point
Return index: string.indexOf(String str);
Return string: String.valueOf(primitive data type x) or Integer.valueOf(int x)
Common methods: split(), replace(), contains()
```