import Streamer
import Audience

if __name__ == '__main__':
    streamer = Streamer.TwitchStreamer("Asia god tone")
    account_no = 0
    god_tone_fan = Audience.TwitchAudience(account_no, "Tommy")
    account_no += 1
    anti_fan = Audience.TwitchAudience(account_no, "Diabetic Audiance")
    account_no += 1

    streamer.registerObserver(god_tone_fan)
    streamer.registerObserver(anti_fan)

    print("Streamer is streaming:")
    streamer.is_streaming = True
    print()

    print("Streamer is off-stream:")
    streamer.is_streaming = False
    print()

    print("Streamer remove anti-fan and start streaming:")
    streamer.removeObserver(anti_fan)
    streamer.is_streaming = True

