# 合成模式 (Composite Pattern)
合成模式允許你將物件合成樹狀結構用以表示 **部分-整體** 的階層架構。同時讓client可以以一致性的方式操作單一物件或合成物件。  
The Composite Pattern allows you to compose objects into tree structures to represent part-whole hierarchies. Composite lets clients treat individual objects and compositions of objects uniformly.


## 分類
1. 結構模式 (Structural patterns)
   - 將物件整理成樹狀結構並統一其行為
1. 物件模式 (Object pattern)
   - 並非透過繼承而是透過聚合來實現


## UML解釋
1. Client持有一個Component物件，並透過這個物件進行一些操作
1. Composite物件實作了Component介面，該物件由Component聚合。該物件的operation由它所持有的components執行。
1. Leaf實作了Component介面。該物件的operation由物件本身執行。


## 範例描述
我們有一個菜單物件，菜單物件的組成包含了**用品項做分類的子菜單**或**單一品項**。菜單物件與單一品項物件都有一個toString方法顯示資訊。菜單物件的toString方法會顯示所有包含的品項的資訊，而單一品項物件的toString只顯示該品項的資訊


## C++相關
1. 範例編譯&執行指令  
cd CompositePattern/cpp/  
g++ main.cpp src/menu.cpp -o main  
./main


## 其它
1. 合成模式可以跟迭代器合在一起使用，可以設計一個合成迭代器去遍歷整棵樹狀結構
2. 若要加強通透性(transparency)的話可以讓leaf與internal node都實作相同介面。但這樣的話leaf對於操作聚合的方法需要考慮設計是否要拋出exception。
3. leaf的迭代器可以設計成空迭代器，該迭代器的hasNext永遠回傳false
4. 若藉由遍歷樹狀結構才能完成某件事情太花時間的話可以在internal node設計一些cache把子樹的結果存起來讓下次呼叫時可以加速。
5. 這個模式常見於GUI相關的設計上。