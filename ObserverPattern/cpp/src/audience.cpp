#include <string>
#include <iostream>
#include "header/audience.h"

using namespace std;

TwitchAudience::TwitchAudience(int accountID, string nickname){
    this->accountID = accountID;
    this->nickname = nickname;
}

void TwitchAudience::update(string streamInfo){
    cout << "\tAudience " << nickname << " receive the message: " << streamInfo << endl;
}