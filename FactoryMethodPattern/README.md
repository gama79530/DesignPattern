# 工廠方法模式(Factory Method Pattern)
工廠方法模式定義了一個用來產生物件的介面，但讓子類別決定要實體化哪種類別。工廠方法把實體化的責任轉移給子類別。  
The Factory Method Pattern defines an interface for creating an object, but lets subclasses decide which class to instantiate. Factory Method lets a class defer instantiation to subclasses.


## 分類
1. 生成模式 (Creational patterns)
   - 工廠方法牽涉到物件實體化
1. 類別模式 (Class pattern)
   - 利用定義抽象方法作為規範實體化過程的介面與利用繼承的方式讓子類別負責實際處理實體化過程


## UML解釋
1. Creator物件藉由factoryMethod負責規範Product物件的生成，實作細節由各個子類別處理


## 範例描述
程式模擬一個連鎖pizza店，總店規設計出PizzaStore類別負責規範orderPizza的程序並保留createPizza讓各分店負責實作這個產生Pizza的過程以因應不同分店的菜單可能提供的品項不一樣。另外為了控管Pizza的品質，因此設計了一個Pizza介面讓所有Pizza有統一規範。


## C++相關
1. 編譯&執行指令  
cd FactoryMethodPattern/cpp/  
g++ main.cpp src/pizza.cpp src/pizza_store.cpp -o main  
./main


## 其它
1. 這個模式比較適用於實體化時不需要大量合成的物件，若物件實體化需要大量合成則採用抽象工廠模式。通常具有這種特性的物件是屬於比較低階的基本類別。
1. 工廠方法未必要定義成抽象方法，也可以定義成普通方法並提供一套預設的實作。
1. 有點像是把樣板方法模式套用到物件實體化上。
