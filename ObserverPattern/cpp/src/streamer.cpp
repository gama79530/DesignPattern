#include <string>
#include <unordered_map>
#include "header/streamer.h"

using namespace std;

bool Streamer::getIsStreaming(){
    return isStreaming;
}

void Streamer::setIsStreaming(bool isStreaming){
    if(this->isStreaming != isStreaming){
        this->isStreaming = isStreaming;
        notifyObserver();
    }
}

TwitchStreamer::TwitchStreamer(string accountInfo){
    this->accountInfo = accountInfo;
}

void TwitchStreamer::registerObserver(shared_ptr<Audience> audience){
    this->audience.insert(audience);
}
    
void TwitchStreamer::removeObserver(shared_ptr<Audience> audience){
    this->audience.erase(audience);
}
    
void TwitchStreamer::notifyObserver(){
    string streamInfo = isStreaming ? "Streamer " + accountInfo + " is streaming now." : "Streamer " + accountInfo + " is off-stream now.";
    for(auto observer=this->audience.begin(); observer != this->audience.end(); observer++){
        (*observer)->update(streamInfo);
    }
}