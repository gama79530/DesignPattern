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
    TwitchAudience(int accountID, string nickname);
    void update(string streamInfo);
    int getAccountID(){return accountID;}
    void setAccountID(int accountID){this->accountID = accountID;}
    string getNickname(){return nickname;}
    void setNickname(string nickname){this->nickname = nickname;}

private:
    int accountID;
    string nickname;
};

#endif