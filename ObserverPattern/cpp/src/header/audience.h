#ifndef AUDIENCE_HEADER_INCLUDED
#define AUDIENCE_HEADER_INCLUDED

#include <string>

using namespace std;

class Audience{
public:
    virtual void update(string streamInfo) = 0;
};

class TwitchAudience: public Audience{
public:
    int accountID;
    string nickname;
    
    TwitchAudience(int accountID, string nickname);
    
    void update(string streamInfo) override;
};

#endif