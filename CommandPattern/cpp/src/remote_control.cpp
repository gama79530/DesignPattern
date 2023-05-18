#include "header/remote_control.h"
#include <iostream>

namespace{
    int FAN_MAX_SPEED = 5;
}

bool Fan::on(){
    if(currentLevel < FAN_MAX_SPEED){
        if(++currentLevel == FAN_MAX_SPEED){
            cout << "The speed of fan is max level (level " << currentLevel << ")" << endl;
        }else{
            cout << "The speed of fan is level " << currentLevel << endl;
        }
        return true; 
    }else{
        cout << "The current level is already maximum." << endl;
        return false;
    }
}

bool Fan::off(){
    if(currentLevel > 0){
        if(--currentLevel == 0){
            cout << "The fan is off" << endl;
        }else{
            cout << "The speed of fan is level " << currentLevel << endl;
        }
        return true; 
    }else{
        cout << "The fan is already off." << endl;
        return false;
    }
}

bool Light::on(){
    if(!isOn){
        cout << "Light on" << endl;
        isOn = true;
        return true;
    }else{
        cout << "Light is already on." << endl;
        return false;
    }
}

bool Light::off(){
    if(isOn){
        cout << "Light off" << endl;
        isOn = false;
        return true;
    }else{
        cout << "Light is already off." << endl;
        return false;
    }
}

FanOffCommand::FanOffCommand(shared_ptr<Receiver> &receiver){
    this->receiver = receiver;
}

void FanOffCommand::execute(){
    hasStatusChange = receiver->off();
}

bool FanOffCommand::undo(){
    if(hasStatusChange){
        cout << "Undo:\t";
        receiver->on();
        return true;
    }

    return false;
}

shared_ptr<Command> FanOffCommand::clone(){
    return shared_ptr<Command>(new FanOffCommand(*this));
}

FanOnCommand::FanOnCommand(shared_ptr<Receiver> &receiver){
    this->receiver = receiver;
}

void FanOnCommand::execute(){
    hasStatusChange = receiver->on();
}

bool FanOnCommand::undo(){
    if(hasStatusChange){
        cout << "Undo:\t";
        receiver->off();
        return true;
    }

    return false;
}

shared_ptr<Command> FanOnCommand::clone(){
    return shared_ptr<Command>(new FanOnCommand(*this));
}

LightOffCommand::LightOffCommand(shared_ptr<Receiver> &receiver){
    this->receiver = receiver;
}

void LightOffCommand::execute(){
    hasStatusChange = receiver->off();
}

bool LightOffCommand::undo(){
    if(hasStatusChange){
        cout << "Undo:\t";
        receiver->on();
        return true;
    }

    return false;
}

shared_ptr<Command> LightOffCommand::clone(){
    return shared_ptr<Command>(new LightOffCommand(*this));
}

LightOnCommand::LightOnCommand(shared_ptr<Receiver> &receiver){
    this->receiver = receiver;
}

void LightOnCommand::execute(){
    hasStatusChange = receiver->on();
}

bool LightOnCommand::undo(){
    if(hasStatusChange){
        cout << "Undo:\t";
        receiver->off();
        return true;
    }

    return false;
}

shared_ptr<Command> LightOnCommand::clone(){
    return shared_ptr<Command>(new LightOnCommand(*this));
}

MacroCommand::MacroCommand(shared_ptr<vector<shared_ptr<Command>>> &commands){
    this->commands = commands;
}

void MacroCommand::execute(){
    history = make_shared<stack<shared_ptr<Command>>>();
    for(auto command = commands->begin(); command != commands->end(); command++){
        (*command)->execute();
        history->push((*command)->clone());
    }
}

bool MacroCommand::undo(){
    bool isActed = false;
    shared_ptr<Command> command;
    while(!history->empty()){
        command = history->top();
        history->pop();
        isActed = isActed || command->undo();
    }

    return isActed;
}

shared_ptr<Command> MacroCommand::clone(){
    return shared_ptr<Command>(new MacroCommand(*this));
}

void RemoteControl::setOnCommand(shared_ptr<Command> command, int slot){
    onCommands[slot] = command;
}

void RemoteControl::setOffCommand(shared_ptr<Command> command, int slot){
    offCommands[slot] = command;
}

void RemoteControl::pressOnButton(int slot){
    onCommands[slot]->execute();
    history.push(onCommands[slot]->clone());
}

void RemoteControl::pressOffButton(int slot){
    offCommands[slot]->execute();
    history.push(offCommands[slot]->clone());
}

void RemoteControl::pressUndo(){
    shared_ptr<Command> command;
    bool isActed = false;
    while(!history.empty() && !isActed){
        command = history.top();
        history.pop();
        isActed = command->undo();
    }
}
