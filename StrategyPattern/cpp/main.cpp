#include "src/header/computer.h"

using namespace std;

int main(){
    Computer computer;
    shared_ptr<CPU> cpu = make_shared<AMD_Ryzen7_3700X>();
    shared_ptr<GPU> gpu = make_shared<NVIDIA_GeForce_GTX_1660_SUPER>();
    
    computer.setCpu(cpu);
    computer.setGpu2(gpu);
    computer.showInfo();

    return 0;
}