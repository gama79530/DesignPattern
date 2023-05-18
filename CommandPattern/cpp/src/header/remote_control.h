#ifndef REMOTE_CONTROL_HEADER_INCLUDED
#define REMOTE_CONTROL_HEADER_INCLUDED

#include <memory>
#include <vector>
#include <stack>

using namespace std;

class Receiver{
public:
    virtual bool on() = 0;
    virtual bool off() = 0;
};

class Fan: public Receiver{
public:
    bool on();
    bool off();
private:
    int currentLevel = 0;
};

class Light: public Receiver{
public:
    bool on();
    bool off();
private:
    bool isOn = false;
};

class Command{
public:
    virtual void execute() = 0;
    virtual bool undo() = 0;
    virtual shared_ptr<Command> clone() = 0;
};

class FanOffCommand: public Command{
public:
    FanOffCommand(shared_ptr<Receiver> &receiver);

    void execute();
    bool undo();
    shared_ptr<Command> clone();

private:
    shared_ptr<Receiver> receiver;
    bool hasStatusChange = false;
};

class FanOnCommand: public Command{
public:
    FanOnCommand(shared_ptr<Receiver> &receiver);

    void execute();
    bool undo();
    shared_ptr<Command> clone();

private:
    shared_ptr<Receiver> receiver;
    bool hasStatusChange = false;
};

class LightOffCommand: public Command{
public:
    LightOffCommand(shared_ptr<Receiver> &receiver);

    void execute();
    bool undo();
    shared_ptr<Command> clone();

private:
    shared_ptr<Receiver> receiver;
    bool hasStatusChange = false;
};

class LightOnCommand: public Command{
public:
    LightOnCommand(shared_ptr<Receiver> &receiver);

    void execute();
    bool undo();
    shared_ptr<Command> clone();

private:
    shared_ptr<Receiver> receiver;
    bool hasStatusChange = false;
};

class MacroCommand: public Command{
public:
    MacroCommand(shared_ptr<vector<shared_ptr<Command>>> &commands);

    void execute();
    bool undo();
    shared_ptr<Command> clone();

private:
    shared_ptr<vector<shared_ptr<Command>>> commands;
    shared_ptr<stack<shared_ptr<Command>>> history;
};

class RemoteControl{
public:
    void setOnCommand(shared_ptr<Command> command, int slot);
    void setOffCommand(shared_ptr<Command> command, int slot);
    void pressOnButton(int slot);
    void pressOffButton(int slot);
    void pressUndo();

private:
    shared_ptr<Command> onCommands[3];
    shared_ptr<Command> offCommands[3];
    stack<shared_ptr<Command>> history;
};

#endif