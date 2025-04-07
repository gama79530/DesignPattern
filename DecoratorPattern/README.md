# 裝飾者模式 (Decorator Pattern)

裝飾者模式可以動態的將額外職責增加到物件上，裝飾者在提供額外功能這件事上提供了比繼承更有彈性的選擇。  
The Decorator Pattern attaches additional responsibilities to an object dynamically. Decorators provide a flexible alternative to subclassing for extending functionality.

## 分類

1. 結構模式(Structural Pattern)
   - 利用裝飾類別**把物件組合**成一個功能更複雜的物件
1. 物件模式 (Object pattern)
   - 藉由合成把物件組合成功能更複雜的物件
   - 包裝內容可以在執行期決定

## UML解釋

1. 最頂層的介面 `Component` 用來描述物件的功能。
2. `BaseComponent` 介面用來表示這類物件是具有基本功能的 `Component` ，這層介面也可以省略不定義直接讓這類物件實作最頂層的 `Component` 介面，但我認為有定義的話對於物件的分類會更清楚。
3. 有一個 `Decorator` 介面用來表示這類物件提供的功能都是額外外掛的功能。

### 其它

1. 這個模式的特點是外掛功能是可選擇但非必需的
1. 這個模式與策略模式最大的不同是`外掛功能的數量並不固定`，若外掛功能數量有明確上限的話也可以採用策略模式的做法
1. 外掛的功能之間可能會有執行順序的差異但對於執行結果應該`盡量避免`有執行順序的相依性，最常見的範例就是 BaseComponent 有某種數值(ex:價錢、戰鬥力等等)可以受 Decorator 影響而增減數值。
1. `java.io` 的設計上大量採用這種模式進行設計

## 範例描述

我們建立了一個 Beverage 介面用來代表飲料，每種飲料都有成本與售價。接著建立了一系列關於咖啡的飲料物件。此外我們的咖啡可以選擇性的加料，因此我們建立了一個 Condiment 介面，並實作一些 Condiment 類別。

## C++ 相關編譯 & 執行指令  

```bash
cd DecoratorPattern/cpp/  
g++ main.cpp src/beverage.cpp -o main  
./main

# or use makefile
cd DecoratorPattern/cpp/  
make
```

## Python相關

1. python 有提供特 Decorator 的語法糖，但該語法被限制只能用 callable object 或 nested function 來實現 Decorator，並且只能將Decorator 套在 function object 上。
