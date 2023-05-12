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

    public int getAccountID() {
        return accountID;
    }

    public void setAccountID(int accountID) {
        this.accountID = accountID;
    }

    public String getNickname() {
        return nickname;
    }

    public void setNickname(String nickname) {
        this.nickname = nickname;
    }
}
