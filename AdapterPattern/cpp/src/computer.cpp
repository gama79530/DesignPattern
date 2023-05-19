#include <iostream>
#include "header/computer.h"

using namespace std;

string AMD_Ryzen7_3700X::showInfo(){
    return "AMD Ryzen7 3700X";
}

string Old_CPU_Adapter::showInfo(){
    return this->getName();
}

string NVIDIA_GeForce_GTX_1660_SUPER::showInfo(){
    return "NVIDIA GeForce GTX 1660 SUPER";
}

shared_ptr<CPU> Computer::getCpu(){
    return cpu;
}

void Computer::setCpu(shared_ptr<CPU> &cpu){
    this->cpu = cpu;
}

shared_ptr<GPU> Computer::getGpu1(){
    return gpu1;
}

void Computer::setGpu1(shared_ptr<GPU> &gpu){
    gpu1 = gpu;
}

shared_ptr<GPU> Computer::getGpu2(){
    return gpu2;
}

void Computer::setGpu2(shared_ptr<GPU> &gpu){
    gpu2 = gpu;
}

void Computer::showInfo(){
    cout << "The component of this computer" << endl;
    cout << "CPU   : " << cpu->showInfo() << endl;
    cout << "GPU 1 : " << (gpu1 == nullptr ? "None" : gpu1->showInfo()) << endl;
    cout << "GPU 2 : " << (gpu2 == nullptr ? "None" : gpu2->showInfo()) << endl;
}