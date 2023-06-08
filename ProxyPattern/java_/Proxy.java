package ProxyPattern.java_;

import java.rmi.Remote;
import java.rmi.RemoteException;

public interface Proxy extends Remote{
    void addBalanceAccount(int balanceAccount) throws RemoteException;
    void subtractBalanceAccount(int balanceAccount) throws RemoteException;
    int getBalanceAccount() throws RemoteException;
}
