#ifndef COMPUTER_HEADER_INCLUDED
#define COMPUTER_HEADER_INCLUDED
#include <string>
#include <memory>

using namespace std;

class CPU{
public:
    virtual string showInfo() = 0;
};

class AMD_Ryzen7_3700X: public CPU{
public:
    string showInfo();
};

class GPU{
public:
    virtual string showInfo() = 0;
};

class NVIDIA_GeForce_GTX_1660_SUPER: public GPU{
public:
    string showInfo();
};


class Computer{
public:
    shared_ptr<CPU> getCpu();
    void setCpu(shared_ptr<CPU> &cpu);
    shared_ptr<GPU> getGpu1();
    void setGpu1(shared_ptr<GPU> &gpu);
    shared_ptr<GPU> getGpu2();
    void setGpu2(shared_ptr<GPU> &gpu);
    void showInfo();
    
private:
    shared_ptr<CPU> cpu;
    shared_ptr<GPU> gpu1;
    shared_ptr<GPU> gpu2;
};

#endif