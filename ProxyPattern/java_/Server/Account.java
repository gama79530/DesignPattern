package ProxyPattern.java_.Server;

public class Account {
    int balance = 0;

    public int getBalance(){
        return balance;
    }

    public void addBalanceAccount(int amount){
        balance += amount;
    }

    public void subtractBalanceAccount(int amount){
        balance -= amount;
    }
}
