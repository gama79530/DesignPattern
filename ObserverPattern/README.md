# 觀察者模式 (Observer Pattern)
觀察者模式定義了物件之間的一對多關係使得當一個物件改變狀態時其餘相依物件都會收到通知並更新。  
The Observer Pattern defines a one-to-many dependency between objects so that when one object changes state, all of its dependents are notified and updated automatically.


## 分類
1. 行為模式 (Behavioral pattern)
   - 重點在可以**主動通知**收到某一物件改變狀態
1. 物件模式 (Object pattern)
   - 藉由合成建立Subject與Observer之間的關係
   - 可以在執行期隨意建立Subject與Observer關係


## UML解釋
1. Subject負責開放登記Observer與移除已登記的Observer
2. Observer提供一個callback function讓Subject在狀態改變時可以主動通知已登記的Observer
3. Observer物件的update()根據參數設計可以分成兩類
   - push: Subject主動傳Observer需要用到的參數
   - pull: 將Subject的reference傳給Observer讓Observer自行從Subject的狀態中獲取所需要的資訊


## 範例描述
我們模擬一個訂閱系統。Subject物件代表一個實況主，Observer物件代表各個訂閱用戶。每當實況主開實況時便會發送主動通知訊息。本範例採用push的方式推播資訊。


## C++相關
1. 編譯&執行指令  
cd ObserverPattern/cpp/  
g++ main.cpp src/audience.cpp src/streamer.cpp -o main  
./main


## 其它
1. 這個模式經常被運用在GUI的Listener上，用來實作監控GUI元件觸發某事件時的反應。GUI元件是個Subject物件，用來對事件做反應動作的Listener是個Observer物件
2. 如果實作觀察者模式的方式很固定也可以直接提供抽象類別或者實作類別而不是提供介面，但這可能會稍微犧牲程式的彈性(Java內建的Observable就是使用這種方式)
