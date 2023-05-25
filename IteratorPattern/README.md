# 迭代器模式 (Iterator Pattern)
迭代器模式提供一個方法在不涉及實作細節的條件下去依序存取聚合中的元素。  
The Iterator Pattern provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation.


## 分類
1. 行為模式 (Behavioral pattern)
   - 著重在**依序存取聚合中的元素**
1. 物件模式 (Object pattern)
   - 透過迭代器去獲得"依序存取聚合中的元素"的能力
   - 迭代器並不透過繼承獲得
   

## UML解釋
1. Iterable類別負責儲存與管理物件的collection，並透過createIterator獲得一個Iterator實體。
1. Iterator負責控制 "遍歷collection"。

## 範例描述
程式模擬一個停了幾輛車的車庫。我們可以查看車庫裡所有的車輛資料

## C++相關
1. 範例編譯&執行指令  
cd IteratorPattern/cpp/  
g++ main.cpp src/vehicle.cpp src/garage.cpp -o main  
./main
1. 在使用template的時候可能會有link error，其主要原因是template工作原理有點類似macro，都是在編譯期將定義展開，最大的不同在於使用template的話compiler可以幫忙做類型檢查
2. [How to Define a Template Class in a .h File and Implement it in a .cpp File](https://www.codeproject.com/Articles/48575/How-to-Define-a-Template-Class-in-a-h-File-and-Imp)提供了三種解決方法，目前測試只有第二種方法能符合目前我們的project的架構。另外兩種方法可能需要搭配專案架構才能用。  
   - 在source檔裡面強迫compiler產生一個會被用到的實體。
   - clinet檔除了include header檔之外把source檔也include
   - header檔也include source檔，並且把source檔從專案中移除(但是檔案要留著)


## python相關
1. 只要實作 \_\_next\_\_ 讓該方法**每次回傳一個物件直到迭代完成後raise StopIteration**的物件就是Iiterator物件。
1. 只要實作 \_\_iter\_\_ 讓該方法**回傳Iterator**物件就是Iterable類別。
1. 只要實作 \_\_getitem\_\_ 讓該方法可以**根據輸入的index回傳物件**的物件就是一個Sequence物件，Sequence本身就是種Iterable物件。
