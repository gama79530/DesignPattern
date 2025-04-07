# 表象模式 (Facade Pattern)

表象模式提供一個將子系統統一整合的的介面。表象介面定義了高階介面使得子系統更方便使用。  
The Facade Pattern provides a unified interface to a set of interfaces in a subsytem. Facade defines a higher level interface that makes the subsystem easier to use.

## 分類

1. 結構模式 (Structural patterns)
   - 將子系統整合包裝成統一功能的介面
1. 類別模式 (Class patterns)
   - Facade 介面與子系統介面之間的關係是在設計Facade 介面時就決定的

## UML解釋

1. Facade 介面負責定義高階方法，這些方法的實作由 Component 各個類別的低階方法去實作。
2. Facade 模式是一種將一組複雜物件操作流程封裝成單一簡化介面的設計模式，讓使用者可以透過這個介面，輕鬆完成原本需要多個步驟才能完成的功能。

## 範例描述

辦公室內有各式各樣的設備，有電燈、冷氣與飲水機。我們要整合這些設備提供一個統一操作的介面。這個介面除了可以各自細微的操作各個設備的設定之外，還可以統一的開關這些設備。

## C++ 相關編譯 & 執行指令  

```bash
cd FacadePattern/cpp/  
g++ main.cpp src/office_device.cpp -o main  
./main

# or use makefile
cd FacadePattern/cpp/  
make
```
