# 代理人模式 (Proxy Pattern)
代理人模式讓某個物件A有代理人物件B，藉以控制其他物件對物件A的接觸。  
The Proxy Pattern provides a surrogate or placeholder for another object to control access to it.


## 分類
1. 結構模式 (Structural patterns)
   - 在實際要操縱的物件與client之間增加一個代理人物件，並透過一些結構化的設計讓代理人可以達成特定效果。
1. 類別模式 (Class patterns)
   - 利用實作代理人介面的物件將**操縱物件**與**實際執行**鬆綁。


## UML解釋
1. Proxy是RealSubject物件的分身，他們繼承自同一個介面。
2. Client目標是要操作RealSubject，但這些操作需要透過Proxy間接達成。


## 範例描述
這是一個遠端代理人的程式範例。Account物件負責在server端處理帳戶金額。Proxy介面定義了遠端代理人提供的方法。Skeletons類別負責實作Proxy介面並透過繼承java.rmi.server.UnicastRemoteObject取得Remote Method Invocation的能力。 Service類別扮演RMI的Registry角色負責並提供Server端的main function。Client類別提供client端的main function，負責取得stub並透過stub作為代理人操作account的餘額。


<!-- ## C++相關 -->
<!-- 1. Server範例編譯&執行指令  
cd ProxyPattern\cpp  
g++ main.cpp src/office_device.cpp -o main  
./Server/main

1. Client範例編譯&執行指令  
cd ProxyPattern\cpp  
./Client/main -->

## Java相關
1. 要先啟動Service後再啟動Client。
1. rmi reference format : "rmi://{host}:{port}/{name}"
1. 可參考[Java RMI學習與解讀](https://iter01.com/634299.html)


## Python相關
1. 要先安裝pyro5  
pip install Pyro5
1. 可參考[Pyro官方tutorial](https://pyro4.readthedocs.io/en/stable/tutorials.html)
1. 要先啟動Service後再啟動Client。


## 其它
1. 根據設定代理人的目的可以將這個模式在區分成下面幾種
   - 遠端代理人(Remote Proxy) : 透過網路代理遠端系統的物件
   - 虛擬代理人(Virtual Proxy) : 透過代理人處理實體化時會較耗費資源的物件，在實體化完成之後就會將請求直接轉給該實體處理。
   - 保護代理人(Protection Proxy) : 根據客戶權限決定是否可存取物件
   - 防火牆代理人(Firewall Proxy) : 控制網路資源的存取，保護內部免於受到外面的侵害。
   - 聰明參考代理人(Smart Reference Proxy) : 當物件被參考到時，進行額外的動作。
   - 備用代理人(Caching Proxy) : 將耗資源的運算結果暫存起來，供後續使用，以減少成本。
   - 同步化代理人(Synchronization Proxy) : 提供安全的存取，讓多個執行緖存取同一個物件時不會出錯。
   - 隱藏複雜代理人(Complexity Hiding Proxy) : 用來對一群複雜的類別，進行複雜度隱藏以及存取控制。有時也被稱為表象代理人(Facade Proxy)。
   - 寫入時複製代理人(Copy-On-Write Proxy): 用來控制物件的複製，將複製的動作拖延到客戶真的需要為止，這是虛擬代理人的變形。
2. 與裝飾者模式的區別在於裝飾者模式是要增加行為，而代理人模式是要控制存取。
3. 與轉接器模式的區別在於Proxy與Subject有實作相同介面，而轉接器模式並沒有。