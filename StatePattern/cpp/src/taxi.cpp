#include <iostream>
#include "header/taxi.h"

shared_ptr<State> OffDutyLights::hailed(Taxi *taxi){
    cout << "\tPassenger board on the taxi." << endl;
    return taxi->onDutyLight;
}

shared_ptr<State> OffDutyLights::drive(Taxi *taxi){
    cout << "\tNo passenger..." << endl;
    return taxi->offDutyLights;
}

shared_ptr<State> OffDutyLights::checkout(Taxi *taxi){
    cout << "\tNo passenger..." << endl;
    return taxi->offDutyLights;
}

shared_ptr<State> OnDutyLight::hailed(Taxi *taxi){
    cout << "\tAlready hailed." << endl;
    return taxi->onDutyLight;
}

shared_ptr<State> OnDutyLight::drive(Taxi *taxi){
    cout << "\tTake passenger to their destination." << endl;
    return taxi->arrived;
}

shared_ptr<State> OnDutyLight::checkout(Taxi *taxi){
    cout << "\tThe passenger's destination is not arrived." << endl;
    return taxi->onDutyLight;

}

shared_ptr<State> Arrived::hailed(Taxi *taxi){
    cout << "\tAlready hailed." << endl;
    return taxi->arrived;
}

shared_ptr<State> Arrived::drive(Taxi *taxi){
    cout << "\tWe are at your destination." << endl;
    return taxi->arrived;
}

shared_ptr<State> Arrived::checkout(Taxi *taxi){
    cout << "\tCheckout the bill." << endl;
    return taxi->offDutyLights;
}

Taxi::Taxi(){
    offDutyLights = make_shared<OffDutyLights>();
    onDutyLight = make_shared<OnDutyLight>();
    arrived = make_shared<Arrived>();
    state = offDutyLights;
}

shared_ptr<State> Taxi::getState(){
    return state;
}

void Taxi::hailed(){
    cout << "Someone hails the taxi." << endl;
    shared_ptr<State> previouState = state;
    state = state->hailed(this);
    if(previouState != state){
        state = state->drive(this);
    }
}

void Taxi::checkout(){
    cout << "The passenger checkout the bill." << endl;
    state = state->checkout(this);
}