#ifndef COMPUTER_HEADER_INCLUDED
#define COMPUTER_HEADER_INCLUDED
#include "CPU.h"
#include "GPU.h"

class Computer{
public:
    CPU& getCpu(){return *cpu;}
    void setCpu(CPU& cpu){this->cpu = &cpu;}
    GPU& getGpu1(){return *gpu1;}
    void setGpu1(GPU& gpu){this->gpu1 = &gpu;}
    GPU& getGpu2(){return *gpu2;}
    void setGpu2(GPU& gpu){this->gpu2 = &gpu;}
    void showInfo();
    
private:
    CPU *cpu = nullptr;
    GPU *gpu1 = nullptr;
    GPU *gpu2 = nullptr;
};

#endif