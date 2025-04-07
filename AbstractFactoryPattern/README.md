# 抽象工廠模式 (Abstract Factory Pattern)

抽象工廠模式提供一個介面用賴建立一些相關或相依的物件家族，而不需要明確指定具體類別。
The Abstract Factory Pattern provides an interface for creating families of related or dependent objects without specifying their concrete classes.

## 分類

1. 生成模式 (Creational patterns)
   - 牽涉到物件實體化
1. 物件模式 (Object pattern)
   - 利用介面規範相關物件的實體化
   - 可在執行其決定要使用哪一個具體的工廠，進而影響相依物件的具體類別為何

## UML解釋

1. 有一個 client 物件負責使用各式各樣的 Product 物件。這些 Products 物件則是通過一系列的介面做抽象定義並提供一系列的實做。
2. 有一個 AbstractFactory 介面負責規範要生產那些 Products 。
3. ConcreteFactory 負責決定要生產那些 ConcreteProduct 。
4. Products 物件有可能是策略模式中某個物件的一部分零件。

### 其它

1. 這個模式比較適用於需要由大量基本類別合成的高階類別。而提供基本類別的實作則常由工廠方法模式去實作。
1. 有點像是把策略模式套用到物件實體化上

## 範例描述

程式模擬一個 Pizza 連鎖店， Pizza 店賣的各種 pizza 必須提供一個可以被查詢原料組成的功能，所以可以很容易的連結到使用策略模式的合成來實現。為此本範例定義了 `Pizza` 介面作為 Pizza 店的產品介面。為了控制 pizza 的食材標準，接著又定義了一個 `Ingredient` 介面用來定義合格食材的標準。為了讓各個分店可以各自管理自己的食材來源，因此接著定義了 `IngredientFactory` 讓各個分店可以在統一的規格下各自管理食材來源。

## C++ 相關編譯 & 執行指令  

```bash
cd AbstractFactoryPattern/cpp/  
g++ main.cpp src/ingredient_factory.cpp src/ingredient.cpp src/pizza_store.cpp src/pizza.cpp -o main  
./main

# or use makefile
cd AbstractFactoryPattern/cpp/  
make
```
