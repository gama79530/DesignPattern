# 獨體模式 (Singleton Pattern)

獨體模式確保類別只會有一個實體，並提供了一個全域存取點。  
The Singleton Pattern ensures a class has only one instance, and provides a global point of access to it.

## 分類

1. 生成模式 (Creational pattern)
   - 重點在可以`主動通知`控制類別讓類別只能有唯一個實體
1. 物件模式 (Object pattern)
   - 執行期動態載入 class 才會影響到是否有實體建立

## UML解釋

1. 提供一個 `static getInstance()` 方法作為獨體的全域存取點。

## 範例描述

範例模擬一個車輛管理程式。車輛管理程式 CarManager 負責掌管所有可用的車輛。每一台車有各自的編號且有個名為 `drive()` 功能。我們可以從 CarManager 那裡租車與還車。並且可以設定有多少量可以出租的車。

### 其它

1. 目前是整個物件的所有 method 共用一把鎖。若存取的物件成員會不同的話可以利用持有多把鎖來提升效能。

## C++ 相關編譯 & 執行指令  

```bash
cd SingletonPattern/cpp/  
g++ main.cpp src/car_management.cpp -o main
./main

# or use makefile
cd SingletonPattern/cpp/  
make
```

### 補充

1. C++ 的 synchronized 要利用 lock 自己做。

## Java相關

1. 要利用 volatile 與雙重檢查來實作 getInstance

## Python相關

1. [Creating a singleton in Python](https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python) 這個討論串提供了好幾種實作方式
1. python 的 synchronized 要利用 lock 自己做
