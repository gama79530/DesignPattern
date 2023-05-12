#include "src/header/streamer.h"
#include "src/header/audience.h"
#include <iostream>

using namespace std;

int main(){
    shared_ptr<Streamer> streamer = make_shared<TwitchStreamer>("Asia god tone");
    int accountNo = 0;
    shared_ptr<Audience> godToneFan = make_shared<TwitchAudience>(accountNo++, "Tommy");
    shared_ptr<Audience> antiFan = make_shared<TwitchAudience>(accountNo++, "Diabetic Audiance");

    streamer->registerObserver(godToneFan);
    streamer->registerObserver(antiFan);

    cout << "Streamer is streaming:" << endl;
    streamer->setIsStreaming(true);
    cout << endl;

    cout << "Streamer is off-stream:" << endl;
    streamer->setIsStreaming(false);
    cout << endl;

    cout << "Streamer remove anti-fan and start streaming:" << endl;
    streamer->removeObserver(antiFan);
    streamer->setIsStreaming(true);

    return 0;
}