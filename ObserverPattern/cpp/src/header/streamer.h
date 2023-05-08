#ifndef STREAMER_HEADER_INCLUDED
#define STREAMER_HEADER_INCLUDED

#include <string>
#include <unordered_set>
#include "audience.h"

using namespace std;

class Streamer{
public:
    string accountInfo;
    virtual void registerObserver(Audience* audience) = 0;
    virtual void removeObserver(Audience* audience) = 0;
    virtual void notifyObserver() = 0;
    bool getIsStreaming(){return isStreaming;}
    void setIsStreaming(bool isStreaming);

protected:
    bool isStreaming = false;
};

class TwitchStreamer: public Streamer{
public:
    TwitchStreamer(string accountInfo);
    void registerObserver(Audience* audience);
    void removeObserver(Audience* audience);
    void notifyObserver();

private:
    unordered_set<Audience*> audience;
};

#endif