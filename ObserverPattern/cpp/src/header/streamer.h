#ifndef STREAMER_HEADER_INCLUDED
#define STREAMER_HEADER_INCLUDED

#include <memory>
#include <string>
#include <unordered_set>
#include "audience.h"

using namespace std;

class Streamer{
public:
    string accountInfo;

    virtual void registerObserver(shared_ptr<Audience> audience) = 0;
    virtual void removeObserver(shared_ptr<Audience> audience) = 0;
    virtual void notifyObserver() = 0;

    bool getIsStreaming();
    void setIsStreaming(bool isStreaming);

protected:
    bool isStreaming = false;
};

class TwitchStreamer: public Streamer{
public:
    TwitchStreamer(string accountInfo);
    
    void registerObserver(shared_ptr<Audience> audience) override;
    void removeObserver(shared_ptr<Audience> audience) override;
    void notifyObserver() override;
    
private:
    unordered_set<shared_ptr<Audience>> audience;
};

#endif