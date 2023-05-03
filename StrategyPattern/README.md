# 策略模式 (Strategy Pattern)
策略模式定義了演算法家族、將其個別封裝且使他們之間可以互相替換。 策略模式使演算法與使用演算法的clients互相獨立。  
The Strategy Pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. Strategy lets the algorithm vary independently from clients that use it.


## 分類
1. 行為模式 (Behavioral pattern)
   - 著重在將演算法與使用它的clients獨立
1. 物件模式 (Object pattern)
   - 藉由合成建立演算法與clients的關係
   - 執行期可以抽換演算法


## UML解釋
1. Client物件負責整合各式各樣的演算法讓其發揮功能
2. 演算法有一個介面，負責定義這些演算法的功能
3. 針對演算法介面有多個可選用的實作可供client物件選用


## 範例描述
我們要組裝一台電腦，我們有一個client物件Computer。該物件負責整合所有零件讓其發揮完整功能。我們實作了一個稱作showInfo的method用來顯示已安裝的配件。另外我們有許多各式各樣的元件，例如CPU、GPU、Memory等等。client有事先決定好數量的插槽可以供我們選用，而每個插槽也有各式各樣對應的配件可以使用。為了簡化範例，我們只做顯示CPU與GPU的部分。


## 其它
1. 設計模式與程式碼的整理擺放架構沒有很直接的相關，但並非完全無關
1. 如何將可以變動更換的部分與可以固定的部分切開需要靠經驗
1. 因為python的function也是物件，因此若演算法物件只提供單一功能的話也可以直接用function做合成而非一定要定義一個class
