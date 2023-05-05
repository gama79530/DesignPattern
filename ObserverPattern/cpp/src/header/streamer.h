#ifndef STREAMER_HEADER_INCLUDED
#define STREAMER_HEADER_INCLUDED

#include <string>
#include <unordered_set>
#include "audience.h"

using namespace std;

class Streamer{
public:
    virtual void registerObserver(Audience& audience) = 0;
    virtual void removeObserver(Audience& audience) = 0;
    virtual void notifyObserver() = 0;
    virtual string getAccountInfo() = 0;
    virtual void setAccountInfo(string accountInfo) = 0;
    virtual bool getIsStreaming() = 0;
    virtual void setIsStreaming(bool isStreaming) = 0;
};

class TwitchStreamer: public Streamer{
public:
    TwitchStreamer(string accountInfo);
    void registerObserver(Audience& audience);
    void removeObserver(Audience& audience);
    void notifyObserver();
    string getAccountInfo(){return accountInfo;}
    void setAccountInfo(string accountInfo){this->accountInfo = accountInfo;}
    bool getIsStreaming(){return isStreaming;}
    void setIsStreaming(bool isStreaming);

private:
    unordered_set<Audience*> audience;
    string accountInfo;
    bool isStreaming;
};

#endif