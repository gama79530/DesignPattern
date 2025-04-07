# 命令模式 (Command Pattern)

命令模式將請求封裝成物件，因而使你可以將不同請求的物件參數化、對請求做 `queueing` 或 `logging` 以及支援`復原`動作。  

The Command Pattern encapsulates a request as an object, thereby letting you parameterize other objects with different requests, queue or log requests, and support undoable operations.

## 分類

1. 行為模式(Behavioral Pattern)
   - 使用本模式的重點在於要區分好`各自物件的責任`並進行解耦
1. 物件模式 (Object pattern)
   - 藉由合成把物件組合成功能更複雜的系統
   - 可以在執行期更改命令的設定(甚至更改命令的設定本身也可以當成是一個命令)

## UML解釋

1. `Client` 負責設定好 `Invoker` 要提供的 `Command` 以及與各個 `Command` 對應負責執行命令的 `Receiver` 。
1. Invoker 的任務有 `作為發送 command 的 controller` 、`管理提供的命令`、以及`管理 request 的發送`。
1. `Comand` 負責觸發 `Receiver` 的行為使 `Receiver` 開始工作。
1. `Receiver` 的介面主要是要規範支援的標準行為有哪些，具體的實做則是要專注在把工作完成以及管理個別物件的狀態。

### 其它

1. 除了標準的單一指令之外可以提供以下兩種指令方便整個系統的操作
   - NoCommand (空指令) : 不做任何動作
   - MacroCommand : 將多個 Command 綁定成一個巨集透過單一個命令一次執行。
1. 支援復原功能
   - Invoker的設計必須做變更， interface 必須多提供一個 `undo()` 讓 Client 呼叫。若要能連續復原的話 Invoker 必須要提供一個 Stack 紀錄 Command 的順序
   - Command 也必須提供 `undo()` 以提供單一指令的復原邏輯。復原有兩種實現方法，一種是Receiver 直接提供一個對稱的 method 供Command 呼叫。另外一種是紀錄 Recever 在執行命令之前的狀態在 `undo` 時恢復狀態
1. 要支援 log 功能的話必須由 Invoker 處理 log 功能。要提供 request queue 的話也必需由invoker 處理
1. 這個模式適合用在功能比較繁雜的系統，功能比較多的系統才會需要有一個專門的 Invoker 負責管理提供的功能，若功能比較單純的話 Invoker 不是必要的class。
1. 關於這個 Pattern 的範例
   - Java 的 Runnable
   - Scheduler
   - 資料庫的 transaction 管理

## 範例描述

程式模擬了一支萬用的遙控器，遙控器有 3 組 on-off 的按鍵，我們可以設定它們的功能。其中 2 組按鍵分別對應到開關燈與電風扇的風速的增減。最後一組的按鍵設定是把前面兩組同時 on 或 off 。

## C++相關編譯 & 執行指令  

```bash
cd CommandPattern/cpp/  
g++ main.cpp src/remote_control.cpp -o main  
./main

# or use makefile
cd CommandPattern/cpp/  
make
```  
