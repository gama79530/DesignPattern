package ObserverPattern.java_.Audience;

public class TwitchAudience implements Audience{
    private int accountID;
    private String nickname;

    public TwitchAudience(int accountID, String nickname) {
        this.accountID = accountID;
        this.nickname = nickname;
    }

    @Override
    public void update(String streamInfo) {
        System.out.println(String.format("\tAudience %s receive the message: %s", nickname, streamInfo));
    }

    @Override
    public boolean equals(Object obj){
        return this.accountID == ((TwitchAudience)obj).getAccountID();
    }

    public int getAccountID() {
        return this.accountID;
    }

    public void setAccountID(int accountID) {
        this.accountID = accountID;
    }

    public String getNickname() {
        return this.nickname;
    }

    public void setNickname(String nickname) {
        this.nickname = nickname;
    }
}
