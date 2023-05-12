# 抽象工廠模式(Abstract Factory Pattern)
抽象工廠模式提供一個介面用賴建立一些相關或相依的物件家族，而不需要明確指定具體類別。
The Abstract Factory Pattern provides an interface for creating families of related or dependent objects without specifying their concrete classes.


## 分類
1. 生成模式 (Creational patterns)
   - 牽涉到物件實體化
1. 物件模式 (Object pattern)
   - 利用介面規範相關物件的實體化
   - 可在執行其決定要使用哪一個具體的工廠，進而影響相依物件的具體類別為何


## UML解釋
1. 有一個client物件負責使用各式各樣的Product物件
2. 有一個AbstractFactory介面負責規範要生產那些Product
3. ConcreteFactory負責決定要生產那些ConcreteProduct


## 範例描述
程式模擬一個Pizza連鎖店，針對各分店的Pizza我們必須要控管Pizza的原料組成，但同時也讓各分店可以各自取得合格的原料，因此我們制訂了負責管控原料的IngredientFactory介面。每個Pizze都有它自己的名稱，並且提供了讓客戶檢視成分的功能。

## C++相關
1. 編譯&執行指令  
cd AbstractFactoryPattern/cpp/  
g++ main.cpp src/ingredient_factory.cpp src/ingredient.cpp src/pizza_store.cpp src/pizza.cpp -o main  
./main


## 其它
1. 這個模式比較適用於需要由大量基本類別合成的高階類別。而提供基本類別的實作則常由工廠方法模式去實作。
1. 有點像是把策略模式套用到物件實體化上