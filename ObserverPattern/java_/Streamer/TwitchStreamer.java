package ObserverPattern.java_.Streamer;
import ObserverPattern.java_.Audience.Audience;
import java.util.*;

public class TwitchStreamer implements Streamer{
    private Set<Audience> audience;
    private String accountInfo;
    private boolean isStreaming;

    public TwitchStreamer(String accountInfo) {
        this.audience = new HashSet<>();
        this.accountInfo = accountInfo;
        this.isStreaming = false;
    }

    @Override
    public void registerObserver(Audience audience) {
        this.audience.add(audience);
    }

    @Override
    public void removeObserver(Audience audience) {
        this.audience.remove(audience);
    }

    @Override
    public void notifyObserver() {
        String streamInfo = isStreaming ? String.format("Streamer %s is streaming now.", accountInfo) : String.format("Streamer %s is off-stream now.", accountInfo);
        for(Audience audience: this.audience){
            audience.update(streamInfo);
        }
    }

    @Override
    public String getAccountInfo() {
        return accountInfo;
    }

    @Override
    public void setAccountInfo(String accountInfo){
        this.accountInfo = accountInfo;
    }

    @Override
    public boolean getIsStreaming() {
        return isStreaming;
    }

    @Override
    public void setIsStreaming(boolean isStreaming){
        if(this.isStreaming != isStreaming){
            this.isStreaming = isStreaming;
            notifyObserver();
        }
    }
}
