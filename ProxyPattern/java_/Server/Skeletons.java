package ProxyPattern.java_.Server;

import java.rmi.*;
import java.rmi.server.*;

import ProxyPattern.java_.Proxy;

public class Skeletons extends UnicastRemoteObject implements Proxy{
    transient private Account account;

    public Skeletons(Account account) throws RemoteException{
        this.account = account;
    }

    @Override
    public void addBalanceAccount(int balanceAccount) throws RemoteException {
        System.out.println(String.format("Proxy add balance account %d", balanceAccount));
        account.addBalanceAccount(balanceAccount);
    }

    @Override
    public void subtractBalanceAccount(int balanceAccount) throws RemoteException {
        System.out.println(String.format("Proxy subtract balance account %d", balanceAccount));
        account.subtractBalanceAccount(balanceAccount);
    }

    @Override
    public int getBalanceAccount() throws RemoteException {
        return account.getBalance();
    }
}
