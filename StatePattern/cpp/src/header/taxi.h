#ifndef TAXI_HEADER_INCLUDED
#define TAXI_HEADER_INCLUDED

#include <memory>

using namespace std;

class Taxi;

class State{
public:
    virtual shared_ptr<State> hailed(Taxi *taxi) = 0;
    virtual shared_ptr<State> drive(Taxi *taxi) = 0;
    virtual shared_ptr<State> checkout(Taxi *taxi) = 0;
};

class OffDutyLights: public State{
public:
    shared_ptr<State> hailed(Taxi *taxi);
    shared_ptr<State> drive(Taxi *taxi);
    shared_ptr<State> checkout(Taxi *taxi);
};

class OnDutyLight: public State{
public:
    shared_ptr<State> hailed(Taxi *taxi);
    shared_ptr<State> drive(Taxi *taxi);
    shared_ptr<State> checkout(Taxi *taxi);
};

class Arrived: public State{
public:
    shared_ptr<State> hailed(Taxi *taxi);
    shared_ptr<State> drive(Taxi *taxi);
    shared_ptr<State> checkout(Taxi *taxi);
};

class Taxi{
public:
    Taxi();
    shared_ptr<State> getState();
    void hailed();
    void checkout();
    
    friend class OffDutyLights;
    friend class OnDutyLight;
    friend class Arrived;

private:
    shared_ptr<State>state;
    shared_ptr<State> offDutyLights;
    shared_ptr<State> onDutyLight;
    shared_ptr<State> arrived;
};

#endif