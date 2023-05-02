package ObserverPattern.java_.Streamer;
import ObserverPattern.java_.Audience.Audience;

public interface Streamer {
    void registerObserver(Audience audience);
    void removeObserver(Audience audience);
    void notifyObserver();
    String getAccountInfo();
    void setAccountInfo(String accountInfo);
    boolean getIsStreaming();
    void setIsStreaming(boolean isStreaming);
}
