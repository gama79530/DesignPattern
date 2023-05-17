# Command Pattern (Behavioral, Object)
命令模式將請求封裝成物件，因而使你可以將不同請求的物件參數化、對請求做queue或log以及支援復原動作。
The Command Pattern encapsulates a request as an object, thereby letting you parameterize other objects with different requests, queue or log requests, and support undoable operations.


## 分類
1. 行為模式(Behavioral Pattern)
   - 使用本模式的重點在於要區分好**各自物件的責任**並進行解耦
1. 物件模式 (Object pattern)
   - 藉由合成把物件組合成功能更複雜的系統
   - 可以在執行期更改命令的設定(甚至更改命令的設定本身也可以當成是一個命令)


## UML解釋
1. Client負責設定好**Invoker要提供的Command**與**要負責執行各個Command的Receiver**
1. Invoker的任務有**作為發送command的interface**、**管理提供的命令**、以及**管理request的發送**
1. Comand負責觸發Receiver的行為使Receiver開始工作
1. Receiver專注在把工作完成

## 範例描述
程式模擬了一支萬用的遙控器，遙控器有3組on-off的按鍵，我們可以設定它們的功能。其中2組按鍵分別對應到開關燈與電風扇的風速的增減。最後一組的按鍵設定是把前面兩組同時on或off。

## C++相關
1. 編譯&執行指令  
cd CommandPattern/cpp/  
g++ main.cpp src/beverage.cpp -o main  
./main


## 其它
1. 除了標準的單一指令之外可以提供以下兩種指令方便整個系統的操作
   - NoCommand (空指令) : 不做任何動作
   - MacroCommand : 將多個Command綁定成一個巨集透過單一個命令一次執行。
1. 支援復原功能
   - Invoker的設計必須做變更，interface必須多提供一個undo()讓Client呼叫。若要能連續復原的話Invoker必須要提供一個Stack紀錄Command的順序
   - Command也必須提供undo()以提供單一指令的復原邏輯。復原有兩種實現方法，一種是Receiver直接提供一個對稱的method供Command呼叫。另外一種是紀錄Recever在執行命令之前的狀態在undo時恢復狀態
1. 要支援log功能的話必須由Invoker處理log功能。要提供request queue的話也必需由invoker處理
1. 這個模式適合用在功能比較繁雜的系統，功能比較多的系統才會需要有一個專門的Invoker負責管理提供的功能，若功能比較單純的話Invoker不是必要的class。
1. 關於這個Pattern的範例
   - Java的Runnable
   - Scheduler
   - 資料庫的transaction管理
