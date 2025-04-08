# 迭代器模式 (Iterator Pattern)

迭代器模式提供一個方法在不涉及實作細節的條件下去依序存取聚合中的元素。  
The Iterator Pattern provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation.

## 分類

1. 行為模式 (Behavioral pattern)
   - 著重在`依序存取聚合中的元素`
1. 物件模式 (Object pattern)
   - 透過迭代器去獲得"依序存取聚合中的元素"的能力
   - 迭代器並不透過繼承獲得

## UML解釋

1. Iterable 類別負責儲存與管理物件的 collection ，並透過 createIterator 獲得一個 Iterator 實體。
1. Iterator 負責控制`遍歷 collection` 。

## 範例描述

程式模擬一個停了幾輛車的車庫。我們可以查看車庫裡所有的車輛資料

## C++ 相關編譯 & 執行指令  

```bash
cd IteratorPattern/cpp/
g++ main.cpp src/vehicle.cpp -Iheader -o main
./main

# or use makefile
cd IteratorPattern/cpp/  
make
```

### 其它補充

1. 在使用 template 的時候可能會有 link error ，其主要原因是 template 工作原理有點類似 macro ，都是在編譯期將定義展開，最大的不同在於使用 template 的話 compiler 可以幫忙做類型檢查。
2. [How to Define a Template Class in a .h File and Implement it in a .cpp File](https://www.codeproject.com/Articles/48575/How-to-Define-a-Template-Class-in-a-h-File-and-Imp) 提供了三種解決方法  
   - 在 header 檔裡面利用一個不會實際使用的global function 去讓 compiler 展開一切可能會用到的 type
   - clinet 檔除了 include header 檔之外把 source 檔也 include
   - header 檔也 include source 檔，並且把 source 檔從專案中移除(但是檔案要留著)
3. chatGPT 提供另外三個解法
   - 直接把 class 的定義寫在 header 裡面，這個是最穩健的作法。
   - 把實做寫在另外一個 `.tpp` 或者 `.impl.h` 裡面然後在 header 裡面 include 這個檔案。
   - 在 `.cpp` 中明確實體化 也就是在 `.cpp` 裡面多加一行 `template class MyTemplate<int>;` 或者 `template class MyTemplate<char>;` 之類會實際使用到的。

## python相關

1. 只要實作 `__next__` 讓該方法每次回傳一個物件直到迭代完成後 `raise StopIteration` 的物件就是 Iiterator 物件。
1. 只要實作 `__iter__` 讓該方法回傳 `Iterator` 物件就是 `Iterable` 類別。
1. 只要實作 `__getitem__` 讓該方法可以根據輸入的 `index` 回傳物件的物件就是一個 `Sequence` 物件， `Sequence` 本身就是種 `Iterable` 物件。
