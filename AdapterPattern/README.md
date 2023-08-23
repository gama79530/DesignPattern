# 轉接器模式 (Adapter Pattern)
轉接器模式將類別的介面傳換成另外一個client預期介面。轉接器讓只因介面不相容而不能一起使用的類別可以一起工作。  
The Adapter Pattern converts the interface of a class into another interface the clients expect. Adapter lets classes work together that couldn’t otherwise because of incompatible interfaces.


## 分類
1. 結構模式 (Structural patterns)
   - 將介面轉換成另外一個介面使得該物件與既有系統相容
1. 物件模式 (Object pattern)、類別模式 (Class patterns)
   - 有兩種方法可以實作轉接器類別

## UML解釋
1. Client依賴Target物件
2. ObjectAdapter利用合成將Adaptee物件轉接
3. ClassAdapter利用**多重繼承**將Adaptee物件轉接


## 範例描述
接續策略模式的範例，今天因為某種原因導致較新的CPU全部斷料。我們只能從老機器上殺肉取得雖然性能不好但至少功能還正常的CPU。但是因為CPU太舊導致無法直接安裝到電腦上，因此我們多了一個轉接器才將CPU裝上電腦。


## C++相關
1. 範例編譯&執行指令  
cd AdapterPattern/cpp/  
g++ main.cpp src/computer.cpp src/lib/old_cpu.cpp -o main  
./main

2. 使用makefile
cd AdapterPattern/cpp/  
make

1. c++版本採用類別轉接器處裡