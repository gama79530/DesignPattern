# 觀察者模式 (Observer Pattern)

觀察者模式定義了物件之間的一對多關係使得當一個物件改變狀態時其餘相依物件都會收到通知並更新。  
The Observer Pattern defines a one-to-many dependency between objects so that when one object changes state, all of its dependents are notified and updated automatically.

## 分類

1. 行為模式 (Behavioral pattern)
   - 重點在可以`主動通知`收到某一物件改變狀態
1. 物件模式 (Object pattern)
   - 藉由合成建立 `Subject` 與 `Observer` 之間的關係
   - 可以在執行期隨意建立 `Subject` 與 `Observer` 關係

## UML解釋

1. Subject 負責開放登記 Observer 與移除已登記的 Observer
2. Observer 提供一個 callback function 讓 Subject 在狀態改變時可以主動通知已登記的 Observer
3. Observer 物件的 `callback function` 根據參數設計可以分成兩類，這個 callback function 的主被動是針對資料更新的推送方式而不是觸發時機。
   - push: Subject 主動推送 Observer 需要用到的參數
   - pull: 將 Subject 的 reference 傳給 Observer 讓 Observer 自行從 Subject 的狀態中獲取所需要的資訊
4. push 的作法必須事先決定要推送哪些資訊，一旦決定了之後就會比較難變更，因為所有的 Observer 都必須要跟著變動。因此使用 pull 的方法會比較具備彈性，但這代表 Observer 有機會可以使用所有 Subject 的 `public member` 。

### 其它

1. 這個模式經常被運用在 GUI 的 Listener 上，用來實作監控 GUI 元件觸發某事件時的反應。 GUI 元件是個 Subject 物件，用來對事件做反應動作的 Listener 是個 Observer 物件
2. 如果實作觀察者模式的方式很固定也可以直接提供抽象類別或者實作類別而不是提供介面，但這可能會稍微犧牲程式的彈性 ( Java 內建的 Observable 就是使用這種方式)

## 範例描述

我們模擬一個訂閱系統。 Subject 物件代表一個實況主， Observer 物件代表各個訂閱用戶。每當實況主開實況時便會發送主動通知訊息。本範例採用 push 的方式推播資訊。

## C++ 相關編譯 & 執行指令  

```bash
cd ObserverPattern/cpp/  
g++ main.cpp src/audience.cpp src/streamer.cpp -o main  
./main

# or use makefile
cd ObserverPattern/cpp/  
make
```
