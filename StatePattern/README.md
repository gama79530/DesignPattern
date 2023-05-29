# 狀態模式 (State Pattern)
狀態模式使物件可以依據在內部狀態改變行為，這讓物件看起來很像是改變了類別。  
The State Pattern allows an object to alter its behavior when its internal state changes. The object will appear to change its class.

## 分類
1. 行為模式 (Behavioral pattern)
   - 重點是依據狀態改變行為
1. 物件模式 (Object pattern)
   - 不透過繼承而是透過合成取得這種能力


## UML解釋
1. Context物件由數個不同的State物件組成。
2. Client向Context發出request，而Context物件的request由他所持有的其中一個State物件執行，並且在執行之後適當的切換狀態。


## 範例描述
程式範例模擬了計程車營業的狀態變化，計程車有3種狀態:空車、載客中、到達目的。計程車提供了叫車與結帳兩個動作。這兩個動作會影響到計程車的狀態變化。

## C++相關
1. 編譯&執行指令  
cd StatePattern/cpp/  
g++ main.cpp src/taxi.cpp -o main  
./main
1. class circular dependency 要靠 forward declaratation解決。
1. share_ptr只能用複製的或者從make_share取得，否則物件的記憶體空間會被錯誤的釋放掉。


# 其它
1. 這個模式有點像是把策略模式利用在狀態機上面。但策略模式通常事由Client去切換演算法，而狀態模式則是而狀態模式則是Context本身會自主切換。
2. 切換狀態的動作可以由Context決定或者由State決定。由Context決定的好處是鬆綁Context與State的關係。而由State做切換的話好處是狀態的切換可以更動態的依據狀態決定。
