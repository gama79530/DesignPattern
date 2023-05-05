#include <string>
#include <unordered_map>
#include "header/streamer.h"

using namespace std;

TwitchStreamer::TwitchStreamer(string accountInfo){
    this->accountInfo = accountInfo;
    isStreaming = false;
}

void TwitchStreamer::registerObserver(Audience& audience){
    this->audience.insert(&audience);
}
    
void TwitchStreamer::removeObserver(Audience& audience){
    this->audience.erase(&audience);
}
    
void TwitchStreamer::notifyObserver(){
    string streamInfo = isStreaming ? "Streamer " + accountInfo + " is streaming now." : "Streamer " + accountInfo + " is off-stream now.";
    for(auto observer=this->audience.begin(); observer != this->audience.end(); observer++){
        (*observer)->update(streamInfo);
    }
}

void TwitchStreamer::setIsStreaming(bool isStreaming){
    if(this->isStreaming != isStreaming){
        this->isStreaming = isStreaming;
        notifyObserver();
    }
}