# 合成模式 (Composite Pattern)

合成模式允許你將物件合成樹狀結構用以表示 `部分 - 整體` 的階層架構。同時讓 client 可以以一致性的方式操作單一物件或合成物件。  
The Composite Pattern allows you to compose objects into tree structures to represent part-whole hierarchies. Composite lets clients treat individual objects and compositions of objects uniformly.

## 分類

1. 結構模式 (Structural patterns)
   - 將物件整理成樹狀結構並統一其行為
1. 物件模式 (Object pattern)
   - 並非透過繼承而是透過聚合來實現

## UML解釋

1. Client 持有一個 Component 物件，並透過這個物件進行一些操作
1. Composite 物件實作了 Component 介面，該物件由 Component 聚合。該物件的 operation 由它所持有的 components 執行。
1. Leaf 實作了 Component 介面。該物件的 operation 由物件本身執行。

### 其它

1. 合成模式可以跟迭代器合在一起使用，可以設計一個合成迭代器去遍歷整棵樹狀結構
2. 若要加強通透性 (transparency) 的話可以讓 leaf 與 internal node 都實作相同介面。但這樣的話 leaf 對於操作聚合的方法需要考慮設計是否要拋出 exception。
3. leaf 的迭代器可以設計成空迭代器，該迭代器的 hasNext 永遠回傳 false
4. 若藉由遍歷樹狀結構才能完成某件事情太花時間的話可以在 internal node 設計一些 cache 把子樹的結果存起來讓下次呼叫時可以加速。
5. 這個模式常見於 GUI 相關的設計上。

## 範例描述

我們有一個菜單物件，菜單物件的組成包含了`用品項做分類的子菜單`或`單一品項`。菜單物件與單一品項物件都有一個 toString 方法顯示資訊。菜單物件的toString 方法會顯示所有包含的品項的資訊，而單一品項物件的 toString 只顯示該品項的資訊

### 補充

1. `MenuBook` 與 `SubMenu` 是在設計架構上有階層關係。但在程式實做架構中實際上並沒有明確的階層關係。
2. 這個 pattern 的特點是所有的 node 都會有一個統一的 interface 做規範。

## C++ 相關編譯 & 執行指令  

```bash
cd CompositePattern/cpp/  
g++ main.cpp src/menu.cpp -o main  
./main

# or use makefile
cd CompositePattern/cpp/  
make
```
