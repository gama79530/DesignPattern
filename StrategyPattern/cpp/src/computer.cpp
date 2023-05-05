#include <iostream>
#include "header/computer.h"

using namespace std;

void Computer::showInfo(){
    cout << "The component of this computer" << endl;
    cout << "CPU   : " << cpu->showInfo() << endl;
    cout << "GPU 1 : " << (gpu1 == nullptr ? "None" : gpu1->showInfo()) << endl;
    cout << "GPU 2 : " << (gpu2 == nullptr ? "None" : gpu2->showInfo()) << endl;
}