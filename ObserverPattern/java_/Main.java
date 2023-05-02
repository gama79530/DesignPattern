package ObserverPattern.java_;
import ObserverPattern.java_.Audience.*;
import ObserverPattern.java_.Streamer.*;

class Main{
    public static void main(String[] args) {
        Streamer streamer = new TwitchStreamer("Asia god tone");
        int accountNo = 0;
        Audience godToneFan = new TwitchAudience(accountNo++, "Tommy");
        Audience antiFan = new TwitchAudience(accountNo++, "Diabetic Audiance");
    
        streamer.registerObserver(godToneFan);
        streamer.registerObserver(antiFan);

        System.out.println("Streamer is streaming:");
        streamer.setIsStreaming(true);
        System.out.println();
        
        System.out.println("Streamer is off-stream:");
        streamer.setIsStreaming(false);
        System.out.println();

        System.out.println("Streamer remove anti-fan and start streaming:");
        streamer.removeObserver(antiFan);
        streamer.setIsStreaming(true);
    }
}