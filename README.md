# Design Pattern
 
## Project說明
1. 這個project主要是要練習一些關於OOP設計模式的例子,提供了C++、Java與Python實作，主要的知識來源是Head First Design Patterns這本書，另外也參考一些網路上的文章。
2. 所有UML與範例都是以Java為基準，其他程式語言的實作可能會因應程式語言的特性而做些微調整

** 目前正在慢慢重構中，有些舊的內容還沒開始重構的會先暫時留著 **


## 設計準則
1. 找出程式中可能需要變動之處並將它們獨立出來。  
Identify the aspects of your application that vary and separate them from what stays the same.
1. 針對介面寫程式而非針對實作而寫。  
Program to an interface, not an implementation.
1. 多用合成，少用繼承。  
Favor composition over inheritance.
1. 盡量鬆綁有互動的物件之間的關係  
Strive for loosely coupled designs between objects that interact.
1. 類別要對擴充開放，對修改內容關閉  
Classes should be open for extension, but closed for modification.


## 模式分類
### 根據目標分類
1. **生成模式 (Creational patterns)**
   - 生成模式牽涉到物件實體化，這類模式都提供一個方式將client端程式從它需要的物件的實體化過程中鬆綁。  
   Creational patterns involve object instantiation and all provide a way to decouple a client from the objects it needs to instantiate.
1. **行為模式 (Behavioral Pattern)**
   - 行為模式重點在類別與物間之間的互動以及各自的責任。  
   Any pattern that is a Behavioral Pattern is concerned with how classes and objects interact and distribute responsibility.
1. **結構模式 (Structural patterns)**
   - 結構模式使programmer可以將物件組合成更大的結構。  
   Structural patterns let you compose classes or objects into larger structures. 

### 根據模式處理的對象
1. **類別模式 (Class patterns)**
   - 類別模式藉由介面描述類別之間的關係。類別之間的關係是在編譯期建立的。  
   Class patterns describe how relationships between classes are defined via inheritance. Relationships in class patterns are established at compile time.
1. **物件模式 (Object patterns)**
   - 物件模式描述了物件之間的關係且主要是藉由合成定義。 物件之間的關係通常是在執行期建立且更動態與更彈性。  
   Object patterns describe relationships between objects and are primarily defined by composition. Relationships in object patterns are typically created at runtime and are more dynamic and flexible.


## Reference
1. [Head First Design Patterns](https://www.oreilly.com/library/view/head-first-design/0596007124/).

------

## Comment
1. As time passing, the problem may not be the same as the original.
1. Only using a certain pattern when current problem is similar to pattern's context. 
1. Using pattern for reusability and more clear structure.

## Design Principle
1. Keep it simple.
1. Take out what you don’t really need.
<!-- ch8 -->
1. Low-level components don't call high-level components.
<!-- ch9 -->
1. A class should have only one reason to change.

## Summary
### What is pattern
1. A _Pattern_ is a **solution** to a **problem** in a **context**.
   - The _context_ is the situation in which the pattern applies. This should be a **recurring** situation.
   - The _problem_ refers to the **goal** you are trying to achieve in this context, but it also refers to any **constraints** that occur in the context.
   - The _solution_ is what you're after: a general design that **anyone can apply** which resolves the goal and set of constraints.

### How to describe design pattern
1. **Pattern name**
1. The **intent** describes what the pattern does in a short statement. You can also think of this as the pattern’s definition.
1. The **motivation** gives you a concrete
scenario that describes the problem and
how the solution solves the problem.
1. The **applicability** describes situations
in which the pattern can be applied.
1. The **structure** provides a diagram illustrating the relationships among the classes that participate
in the pattern.
1. The **participants** are the classes and
objects in the design. This section describes their responsibilities and roles in the pattern.
1. **Collaborations** tells us how the participants work together in the pattern.
1. The **consequences** describe the effects that using this pattern may have: good and bad.
1. **Implementation / Sample code**
1. **Known uses** describes examples of this pattern
found in real systems.
1. **Related patterns** describes the relationship between this pattern and others.