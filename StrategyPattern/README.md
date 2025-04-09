# 策略模式 (Strategy Pattern)

策略模式`定義`了演算法家族、將其各別`封裝`且使他們之間可以互相替換。 策略模式使演算法與使用演算法的 clients 互相獨立。  
The Strategy Pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. Strategy lets the algorithm vary independently from clients that use it.

## 分類

1. 行為模式 (Behavioral pattern)
   - 著重在將演算法與使用它的clients獨立讓其各自負擔其責任
1. 物件模式 (Object pattern)
   - 藉由合成建立演算法與clients的關係
   - 執行期可以抽換演算法

## UML解釋

1. Client 物件負責整合各式各樣的演算法讓其發揮功能
2. 演算法有一個介面，負責定義這些演算法的功能
3. 針對演算法介面有多個可選用的實作可供 client 物件選用

## 範例描述

我們要組裝一台電腦，我們有一個 client 物件 `Computer` 。該物件負責整合所有零件讓其發揮完整功能。我們實作了一個稱作 `showInfo` 的 method 用來顯示已安裝的配件。另外我們有許多各式各樣的元件，例如 CPU 、 GPU 、 Memory 等等。 client 有事先決定好數量的插槽可以供我們選用，而每個插槽也有各式各樣對應的配件可以使用。為了簡化範例，我們只做顯示 CPU 與 GPU 的部分。

### 其它

1. `區分可變動的部分將其封裝成演算法家族`這件事仰賴於經驗

## C++ 相關編譯 & 執行指令  

```bash
cd StrategyPattern/cpp/  
g++ main.cpp src/computer.cpp -o main  
./main

# or use makefile
cd StrategyPattern/cpp/  
make
```

### 補充

1. 因為 C++ 有 `function pointer` 可以使用，因此演算法也可以使用 function 與 function pointer 來搭配完成合成。
2. 利用 C++ 的 smart pointer 會比較容易避免 `memory leak` 。

## python相關

1. 因為 python 的 function 也是物件，因此若演算法物件只提供單一功能的話也可以直接用 function 做合成而非一定要定義一個 class
