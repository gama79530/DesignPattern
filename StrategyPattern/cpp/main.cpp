#include "src/header/computer.h"
#include "src/header/CPU.h"
#include "src/header/GPU.h"

using namespace std;

int main(){
    Computer computer;
    AMD_Ryzen7_3700X cpu;
    NVIDIA_GeForce_GTX_1660_SUPER gpu2;
    computer.setCpu(cpu);
    computer.setGpu2(gpu2);
    computer.showInfo();

    return 0;
}