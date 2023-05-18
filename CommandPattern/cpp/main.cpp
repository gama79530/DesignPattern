#include "src/header/remote_control.h"
#include <iostream>


int main(){
    shared_ptr<Receiver> light = make_shared<Light>();
    shared_ptr<Receiver> fan = make_shared<Fan>();

    shared_ptr<RemoteControl> remoteControl = make_shared<RemoteControl>();
    shared_ptr<vector<shared_ptr<Command>>> commands = make_shared<vector<shared_ptr<Command>>>();
    commands->push_back(make_shared<LightOnCommand>(light));
    commands->push_back(make_shared<FanOnCommand>(fan));
    remoteControl->setOnCommand(make_shared<LightOnCommand>(light), 0);
    remoteControl->setOnCommand(make_shared<FanOnCommand>(fan), 1);
    remoteControl->setOnCommand(make_shared<MacroCommand>(commands), 2);
    
    commands = make_shared<vector<shared_ptr<Command>>>();
    commands->push_back(make_shared<LightOffCommand>(light));
    commands->push_back(make_shared<FanOffCommand>(fan));
    remoteControl->setOffCommand(make_shared<LightOffCommand>(light), 0);
    remoteControl->setOffCommand(make_shared<FanOffCommand>(fan), 1);
    remoteControl->setOffCommand(make_shared<MacroCommand>(commands), 2);

    cout << "Button set 1" << endl;
    remoteControl->pressOnButton(0);
    remoteControl->pressOffButton(0);

    cout << "\nButton set 2" << endl;
    remoteControl->pressOnButton(1);
    remoteControl->pressOnButton(1);
    remoteControl->pressOnButton(1);
    remoteControl->pressOnButton(1);
    remoteControl->pressOnButton(1);
    remoteControl->pressOnButton(1);
    remoteControl->pressOffButton(1);
    remoteControl->pressUndo();

    cout << "\nButton set 3" << endl;
    remoteControl->pressOnButton(2);
    remoteControl->pressOffButton(2);
    remoteControl->pressOffButton(2);
    remoteControl->pressUndo();
    remoteControl->pressUndo();
    remoteControl->pressUndo();
    remoteControl->pressUndo();
    
    return 0;
}