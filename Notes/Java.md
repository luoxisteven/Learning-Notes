# Java

重点记忆:
   - **面向对象编程 (Object-Oriented Programming)**
   - **Java 三大特性 (封装，继承，多态)**
   - **修饰符 (default, public, private, protected)**
   - **关键字 (abstract, static, synchronized, transient, volatile)**
   - **Package 打包**

## Java 三大特性 (封装，继承，多态)

### 封装 (Encapsulation)
   - 隐藏对象的内部实现细节，仅对外暴露必要的接口。
   - 通过访问修饰符（如`private`、`public`、`protected`）来实现。

### 多态 (Polymorphism)
   通过 `重载 Overload ` 和 `重写 Override`实现。
   1) `Override 重写`:
      - 子类对父类允许访问的方法进行重新实现，返回值和形参都不能改变。
   2) `Overload 重载`:
      - 同一个类中，方法名字相同，但参数不同。返回类型可以相同也可以不同。

### 继承 (Inheritance)
   - 子类可以继承父类的属性和方法，从而复用父类的功能，并在此基础上扩展或重写已有方法。
   - `extends`: 继承父类的属性和方法。
      - 规则1: 单继承一个类只能有一个直接父类，`只能extends一个父类`。
      - 规则2: 继承父类的属性和方法，但`不继承构造方法`。
      - 规则3: 子类可以使用`super()调用父类的构造方法`。
      - 规则4: `子子类可以调用父父类的接口。`（不支持多继承，支持多重继承）

## Implements 实现接口 Interface
   - 对于接口Interface，我的理解就是一开始把这个需求写出来，可以更好的让不同的编程人员，进行并行开发，有利于效率。
   - 接口定义的是“是什么”而不是“如何做”，`用于描述类的行为能力而不是实现细节`。
   - 和`extends`继承多个不一样，接口可以`implements多个`。
   - 接口类interface不能被实例化。
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


## 数据类型
- 1 Byte = 8 bits
- **short**: 2 Bytes
- **int**: 4 Bytes
- **long**: 8 Bytes
- **float**: 4 Bytes
- **double**: 8 Bytes
- **boolean**: 1 bit
- **char**: 2 Bytes

## 修饰符
- **Default**: 默认类（什么都不写），同一包内任意访问，不同包内不能访问
- **Public**：不同包之间也可以访问
- **Private**：只有当前类可以访问，同一个包不同类也不可以访问
- **Protected**：它和default一样都是用在同一包内任意访问，它不可以被包pacakge外直接访问，需要用到继承的方法来访问。
   ```java
   package otherpackage;

   import mypackage.ParentClass;

   public class ChildClass extends ParentClass {
      public void accessProtectedMember() {
         System.out.println(protectedField); // 子类访问父类的受保护字段
         protectedMethod(); // 子类访问父类的受保护方法
      }
   }
   ```

## Package 打包
把各个类class打包成一个package包，比方说：`com.example.myapp`。同一个包的各个类class，可以相互引用。那当我import的时候，我可以引用某个包的类，如`import java.util.ArrayList;`，我也可以引用整个包`import java.util.*;`，但是不推荐。

如果要用同一个名字的类，要用`包的全限定名称`来进行区分。如：
```java
import java.util.Date; // 导入 java.util 包中的 Date 类

public class DateExample {
    public static void main(String[] args) {
        // 使用导入的 java.util.Date 类
        Date utilDate = new Date();
        System.out.println("java.util.Date: " + utilDate);

        // 使用全限定名称来使用 java.sql.Date 类
        java.sql.Date sqlDate = new java.sql.Date(System.currentTimeMillis());
        System.out.println("java.sql.Date: " + sqlDate);
    }
}
```

## 关键字
- **abstract 抽象**
   - abstract类通过extends继承
   ```java
   public abstract class Animal {
      // 抽象方法，没有方法体
      public abstract void makeSound();

      // 具体方法，包含方法体
      public void sleep() {
         System.out.println("Sleeping...");
      }
   }
   public class Dog extends Animal {}
   ```
- **static 静态**: 
   ```java
   // 1) 静态变量：修饰变量，整个类的所有实例共享相同的值。
   public class MyClass {
      static int staticCounter2 = 0; // 共享的静态变量
      public void abc() {
         //在方法里面定义静态变量会compile失败
         static int staticCounter2;
    }
   }

   // 2) 静态方法：可以在类上直接调用不用创建实例。
   public class Utility {
      public static int add(int a, int b) {
         return a + b;
      }
   }
   // 调用静态方法
   int result = Utility.add(5, 3);

   // 3) 静态代码块：静态代码块在类加载时执行一次，常用于初始化静态变量或执行一些只需运行一次的代码。
   public class MyClass {
      static int staticVar;
      static {
         staticVar = 10; // 静态代码块用于初始化
         System.out.println("静态代码块被调用！");
      }
   }

   // 4) 静态内部类：静态内部类是没有对外部类的实例引用的内部类，可以独立于外部类的实例创建。
   public class OuterClass {
      static class InnerClass {
         public void display() {
               System.out.println("静态内部类的方法被调用！");
         }
      }
   }
   // 调用静态内部类
   OuterClass.InnerClass inner = new OuterClass.InnerClass();
   inner.display();
   ```
- **synchronized**
   - 在方法声明中使用 synchronized关键字，整个方法会在对象级别上加锁。
   - 对于同一个实例instance，同一时刻只有一个线程可以访问这个方法，其他线程需要等待锁释放。
   - `对于不同实例，不同实例间的锁不会相互干扰，所以可以同时访问这个方法。`

- **transient**
   - 在序列化 (Serialization) 过程中被忽略, 修饰的变量不会被持久化(Persistence)。
   ```java
   // 用 ObjectOutputStream，输出这个变量，为null
   private transient String password;
   ```

- **volatile**
   - 当一个线程修改了volatile变量的值，其他线程能够立即看到这个更新的值。
   - 这个volatile变量的值是强制

## 注释
```java
// 这是一个单行注释

/*
这是一个多行注释
可以用来注释多行代码
*/
int y = 20; // 初始化一个变量y为20

/**
 * 这是一个文档注释示例
 * 它通常包含有关类、方法或字段的详细信息
 */
public class MyClass {
    // 类的成员和方法
}
```

## 代码块
- 代码块就是用`{ }`包裹起来的一段代码
   1) **普通代码块**
      - Java在一般情况下由`{ }`包裹起来，这个就是普通代码块
   2) **静态代码块**
      - 在加载类时会执行一些初始化操作。这些操作例如给静态变量（类变量）赋值，或者输出一些东西。`静态代码块只执行一次，无论创建多少个该类的对象。`
      ```java
      public class MyClass {
         static int staticCounter;
         static {
            staticCounter = 1;
            System.out.println("Static block executed.");
         }
      }
      MyClass myClass = new MyClass()
      ```
   3) **实例初始化代码块**
      - 没有 static 关键字，直接放在类中，但在构造方法之前执行，`每次创建对象时都会执行`。
      ```java
      public class MyClass {
         {
            System.out.println("Instance block executed.");
         }
      }
      ```
   4) **同步代码块**
      - 用于多线程环境中，在代码前加上 `synchronized` 关键字，使代码块内的内容在同一时间只能被一个线程访问。
      ```java
      public void syncMethod() {
         synchronized (this) {
            // code inside synchronized block
         }
      }
      ```


## 数组 Array
```java
dataType[] arrayRefVar;
arrayRefVar.length;  // 获取数组长度
string.length();  // 获取字符串长度，注意与数组不同
Array.sort();
Array.equals();
```

## String
``` java
长度: string.length();
检索: string.charAt(int i); // 重点
返回索引: string.indexOf(String str);
返回字符串: String.valueOf(primitive data type x) 或 Integer.valueOf(int x)
常用方法: split(), replace(), contains()
```

## ArrayList
- **Colletions.sort()**
- **add(obj)**: 添加元素
- **get(index)**: 获取指定位置的元素
- **set(index, obj)**: 设置指定位置的元素
- **remove(index)**: 删除指定位置的元素
- **size()**: 获取列表大小
- **contains(obj)**: 判断列表是否包含某个元素
- **indexOf(obj)**: 获取某元素的索引位置
- **toArray()**: 转换为数组


## HashSet
- **add(obj)**: 添加元素
- **contains(obj)**: 判断是否包含元素
- **remove(obj)**: 移除元素
- **size()**: 获取集合大小


## HashMap
- **put(key, value)**: 插入键值对
- **get(key)**: 获取指定键对应的值
- **getOrDefault(key, defaultValue)**: 获取指定键对应的值，若不存在则返回默认值
- **remove(key)**: 删除指定键的键值对
- **size()**: 获取键值对数量
- **containsKey(key)**: 判断是否包含指定键
- **containsValue(value)**: 判断是否包含指定值
- **keySet()**: 获取所有键的集合
- **values()**: 获取所有值的集合


## Iterator 迭代器
迭代器用于遍历集合，最常用的方法有以下几个：
1. **next()**: 返回迭代器的下一个元素，并将指针移到下一个位置。
2. **hasNext()**: 判断集合中是否还有下一个元素。
3. **remove()**: 从集合中删除迭代器最后访问的元素（可选操作）。

> **注意**: 使用传统的迭代方法删除数组元素会导致错误，使用迭代器可以安全地在迭代过程中删除元素。


## 进程和线程

- **进程**是一个“执行的程序”，一个执行的程序可以包含多个线程。
- **线程**是程序运行的最小单位，也是 CPU 调度的最小单位。


---

### 事务的四大特性：ACID

1. **原子性**：每个事务都是一个整体，不可再拆分。事务中的 SQL 语句要么都执行成功，要么都执行失败。
2. **一致性**：事务执行前后数据库的状态保持一致。比如不管如何转账，转账前后的总金额保持不变。
3. **隔离性**：事务和事务之间保持隔离，互不影响。
4. **持久性**：事务一旦提交，对数据库的修改是永久的，即使系统故障也不会影响这些修改。

---

### CAP 定理

1. **一致性 (Consistency)**：所有节点在同一时间拥有相同的数据。这意味着操作的结果必须对所有节点可见。
2. **可用性 (Availability)**：每个请求都必须得到响应，无论成功或失败，系统必须确保所有操作能在有限的时间内完成。
3. **分区容错性 (Partition Tolerance)**：系统能够在出现网络分区的情况下继续运行，即使某些节点无法通信。

---

### 事务隔离性与并发问题

事务的隔离性是指事务之间互不影响，但在实际中多个事务可能同时操作同一数据，导致并发问题：

1. **脏读**：一个事务读取到另一个事务尚未提交的数据。
2. **不可重复读**：一个事务在多次读取同一数据时，得到的结果不一致，因为另一个事务修改了该数据。
3. **幻读**：一个事务读取到的记录条数在多次读取时不一致，因为另一个事务插入或删除了记录。

### 不可重复读与幻读的区别

1. **不可重复读**：是因为另一个事务修改了数据，导致多次读取的值不一致。
2. **幻读**：是因为另一个事务插入或删除了记录，导致多次读取的记录数不一致。

---

### 数据库隔离级别

1. **读未提交 (Read Uncommitted)**：
   - 事务中的修改即使没有提交，其他事务也能看到。
   - 可能发生脏读、不可重复读、幻读。

2. **读已提交 (Read Committed)**：
   - 事务中的修改只有在提交后，其他事务才能看到。
   - 可能发生不可重复读和幻读。

3. **可重复读 (Repeatable Read)**：
   - 该级别保证了每次读取的记录结果一致。
   - 可能发生幻读。

4. **串行化 (Serializable)**：
   - 事务串行执行，能解决所有并发问题，但效率低下，适用于并发量小且需要绝对数据一致性的情况。

---

## Iterator 迭代器

1. **next()**：返回迭代器的下一个元素，并将指针移到下一个位置。
2. **hasNext()**：判断集合中是否还有下一个元素可供访问。
3. **remove()**：从集合中删除迭代器最后访问的元素（可选操作）。

使用迭代器可以在迭代过程中安全地删除元素，避免传统遍历方法可能出现的错误。


## Spring

* 编程式：自己写代码实现功能
* 声明式：通过配置让框架实现功能

   ### 1. Service 层：业务层
   - **功能**：控制业务逻辑
   - **职责**：业务模块的逻辑功能设计。先设计接口，再创建实现类，然后在配置文件中配置其实现关联。Service 层调用 DAO 层的接口进行业务逻辑处理。
   - **好处**：封装 Service 层的业务逻辑有助于业务逻辑的独立性和复用性。

   ### 2. Controller 层：控制层
   - **功能**：调用 Service 层方法来控制业务逻辑
   - **职责**：Controller 层主要调用 Service 层的接口，控制具体的业务流程。配置文件中需对 Controller 层进行相应的配置。
   - **区别**：
   - **Controller**：负责具体业务模块流程的控制
   - **Service**：负责业务模块的逻辑设计

   ### 3. Dao 层：持久层
   - **功能**：与数据库交互
   - **职责**：Dao 层首先创建 Dao 接口，并在配置文件中定义该接口的实现类。模块中可以调用 Dao 接口进行数据处理，而不需关心具体的实现类。Dao 层的数据源和数据库连接参数都在配置文件中进行配置。

   ### 4. Entity 层：实体层
   - **功能**：用于数据库在项目中的类
   - **职责**：定义与数据库表对应的属性，提供 `get` 和 `set` 方法、`toString()` 方法、有参和无参构造函数。


   ### Bean 概念
   在 Spring 框架中，**bean** 是一个非常重要的概念，它代表了应用程序中的一个组件或对象。从概念上讲，bean 是由 Spring 容器实例化、组装和管理的对象。它们是应用程序的核心构建块，通过**依赖注入 (Dependency Injection, DI)** 的方式被引入和使用。

---

   ### Spring 框架概述
   **Spring 框架** 是一个开源的 Java 应用开发框架，提供了一种便捷的方式来创建和管理对象。它使用了**控制反转 (Inversion of Control, IoC)** 和 **依赖注入 (Dependency Injection, DI)** 的原理来简化对象的创建和依赖管理。

---

### 控制反转 (Inversion of Control, IoC)
**控制反转 (IoC)** 是指将对象的创建和依赖关系的管理从应用程序代码中转移到框架中进行。在传统开发模式中，应用程序代码直接负责对象的创建，而在 Spring 中，**Spring 容器**负责对象的实例化、生命周期管理和依赖关系注入。

- **控制反转的目标**：
  - 降低程序耦合度
  - 提高程序的扩展能力

#### 控制反转的具体表现：
1. **对象的创建权利反转**：对象的创建由应用程序代码交给 Spring 容器负责。
2. **对象关系的维护反转**：对象之间的依赖关系由 Spring 容器来管理。

---

### 依赖注入 (Dependency Injection, DI)
**依赖注入 (DI)** 是指在对象创建时，将对象所依赖的其他对象的引用注入到该对象中。Spring 容器通过读取配置文件或使用注解的方式识别对象及其依赖关系，并在对象创建时自动完成依赖注入。这样，对象之间的依赖关系无需显式地在代码中创建和管理，而是由 Spring 容器自动完成。

---

### IoC 容器管理的 Java 对象为 Bean
- Spring 中的 IoC 容器管理的 Java 对象称为 **Bean**。
- 控制反转的核心思想是将对象的创建和依赖管理交给 Spring 容器，以减少代码的耦合并提高灵活性。


### Spring 注解与依赖注入

#### @Autowire 注解
- **默认 byType**：根据类型匹配 IoC 容器中的某个兼容类型的 bean，为属性自动赋值。
- **byType**：通过类型匹配自动注入 Bean。
- **byName**：如果使用 `@Qualifier` 注解，则根据 Bean 的名称匹配。

#### @Resource 注解
- **默认 byName**：根据名称装配。如果未指定 `name` 属性，使用属性名作为名称进行装配。
- **byType**：如果通过名称找不到匹配的 Bean，会自动启动通过类型进行匹配。

---

### 定义 Bean 注解

- **@Component**：标识一个组件类，将其注册为 Spring 的一个 Bean。
- **@Repository**：用于标识 Dao 层的组件，专注于数据持久化操作。
- **@Service**：用于标识 Service 层的组件，负责业务逻辑处理。
- **@Controller**：用于标识 SpringMVC 的 Controller 层，负责处理用户请求和返回结果。

---

### 数据持久化 (Data Persistence)
**数据持久化**是指将数据长期保存到计算机系统中的过程与技术。它确保数据在程序结束或系统重启后依然能够保留并重新加载。

---

### 对象关系映射 (ORM)
**对象关系映射 (Object-Relational Mapping, ORM)** 框架用于将程序中的对象与数据库中的关系数据映射，简化数据访问和持久化操作。

#### 反射机制
**反射机制**是指程序在运行时可以获取自身信息的能力，包括类的属性、方法、构造函数等。这为动态操作提供了强大的灵活性和可扩展性。
