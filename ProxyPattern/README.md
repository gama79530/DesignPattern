# 代理人模式 (Proxy Pattern)

代理人模式讓某個物件 A 有代理人物件 B ，藉以控制其他物件對物件 A 的接觸。  
The Proxy Pattern provides a surrogate or placeholder for another object to control access to it.

## 分類

1. 結構模式 (Structural patterns)
   - 在實際要操縱的物件與client之間增加一個代理人物件，並透過一些結構化的設計讓代理人可以達成特定效果。
1. 類別模式 (Class patterns)
   - 利用實作代理人介面的物件將`操縱物件`與`實際執行`鬆綁。

## UML解釋

1. Proxy 是 RealSubject 物件的分身，他們繼承自同一個介面。
2. Client 目標是要操作 RealSubject ，但這些操作需要透過 Proxy 間接達成。

### 其它

1. 根據設定代理人的目的可以將這個模式在區分成下面幾種
   - 遠端代理人 ( Remote Proxy ) : 透過網路代理遠端系統的物件
   - 虛擬代理人 ( Virtual Proxy ) : 透過代理人處理實體化時會較耗費資源的物件，在實體化完成之後就會將請求直接轉給該實體處理。
   - 保護代理人 ( Protection Proxy ) : 根據客戶權限決定是否可存取物件
   - 防火牆代理人 ( Firewall Proxy ) : 控制網路資源的存取，保護內部免於受到外面的侵害。
   - 聰明參考代理人 ( Smart Reference Proxy ) : 當物件被參考到時，進行額外的動作。
   - 備用代理人 ( Caching Proxy ) : 將耗資源的運算結果暫存起來，供後續使用，以減少成本。
   - 同步化代理人 ( Synchronization Proxy ) : 提供安全的存取，讓多個執行緖存取同一個物件時不會出錯。
   - 隱藏複雜代理人 ( Complexity Hiding Proxy ) : 用來對一群複雜的類別，進行複雜度隱藏以及存取控制。有時也被稱為表象代理人 ( Facade Proxy ) 。
   - 寫入時複製代理人 ( Copy-On-Write Proxy ) : 用來控制物件的複製，將複製的動作拖延到客戶真的需要為止，這是虛擬代理人的變形。
2. 與裝飾者模式的區別在於裝飾者模式是要增加行為，而代理人模式是要控制存取。
3. 與轉接器模式的區別在於 Proxy 與 Subject 有實作相同介面，而轉接器模式並沒有。

## 範例描述

這是一個遠端代理人的程式範例。 Account 物件負責在 server 端處理帳戶金額。 Proxy 介面定義了遠端代理人提供的方法。 Skeletons 類別負責實作 Proxy 介面並透過繼承 `java.rmi.server.UnicastRemoteObject` 取得 Remote Method Invocation 的能力。 Service 類別扮演 RMI 的 Registry 角色負責並提供 Server 端的 main function 。 Client 類別提供 client 端的 main function ，負責取得 stub 並透過 stub 作為代理人操作 account 的餘額。

## C++ 相關編譯 & 執行指令  

這段還沒做。

## Java相關

1. 要先啟動 Service 後再啟動 Client。
1. rmi reference format : "rmi://{host}:{port}/{name}"
1. 可參考[Java RMI學習與解讀](https://iter01.com/634299.html)

## Python相關

1. 要先安裝pyro5  
pip install Pyro5
1. 可參考[Pyro官方tutorial](https://pyro4.readthedocs.io/en/stable/tutorials.html)
1. 要先啟動 Service 後再啟動 Client。
