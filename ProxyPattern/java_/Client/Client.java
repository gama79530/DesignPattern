package ProxyPattern.java_.Client;

import java.rmi.registry.*;
import ProxyPattern.java_.Proxy;

public class Client{
    public static void main(String[] args) throws Exception {
        String host = "127.0.0.1";
        int port = 1099;
        Registry registry = LocateRegistry.getRegistry(host, port);
        Proxy stub = (Proxy) registry.lookup("accountProxy");
        int amount;

        amount = 1000;
        System.out.println(String.format("Add Balance Account: %d", amount));
        stub.addBalanceAccount(amount);
        System.out.println(String.format("Current balance account: %d", stub.getBalanceAccount()));    
        
        amount = 100;
        System.out.println(String.format("Subtract Balance Account: %d", amount));
        stub.subtractBalanceAccount(amount);
        System.out.println(String.format("Current balance account: %d", stub.getBalanceAccount()));    
    }
}
