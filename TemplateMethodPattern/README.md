# 樣板方法模式 (Template Method Pattern)
樣板方法模式將演算法的框架定義到一個method中並轉移部份步驟給子類別。樣板方法讓子類別可以在不改變演算法架構的狀況下重新定義演算法的一些特定步驟。  
The Template Method Pattern defines the skeleton of an algorithm in a method, deferring some steps to subclasses. Template Method lets subclasses redefine certain steps of an algorithm without changing the algorithm’s structure.


## 分類
1. 行為模式 (Behavioral pattern)
   - 著重在讓演算法的部分步驟可以被替換
1. 類別模式 (Class pattern)
   - 藉由繼承去更換演算法的特定步驟


## UML解釋
1. Algorithm Skelton類別定義了演算法的框架，其中的algorithm為樣板方法，該方法會依序呼叫stepA、stepB與stepC。
2. 子類別負責提供stepA、stepB與stepC的實作
3. Algorithm Skelton也可以提供stepA、stepB與stepC的實作作為預設行為。拆分成很多步驟的目的是要讓子類別可以選擇性更改。


## 範例描述
程式使用了BFS與DFS兩種演算法去解LeetCode問題 [226.Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)。系統接受一個用list表示的二元樹。我們的演算法先將陣列轉換成標準的樹狀結構後完成題目要求的左右反轉後再將這個結果轉換回陣列。


## C++相關
1. 範例編譯&執行指令  
cd TemplateMethodPattern/cpp/  
g++ main.cpp src/solution.cpp -o main  
./main

2. 使用makefile
cd TemplateMethodPattern/cpp/  
make

## 其它
1. 樣板方法執行的過程中可以增加一些基於某個method回傳的boolean決定要不要執行另外一個步驟的if語句。這個回傳boolean值的method稱為掛勾(hook)。我們可以在子類別推翻這個方法來決定要不要使用掛勾。
1. 演算法步驟要切割多細是在**實作複雜度**與**變更彈性**之間做trade-off。