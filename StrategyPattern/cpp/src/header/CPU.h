#ifndef CPU_HEADER_INCLUDED
#define CPU_HEADER_INCLUDED
#include <string>

using namespace std;

class CPU{
public:
    virtual string showInfo() = 0;
};

class AMD_Ryzen7_3700X: public CPU{
public:
    string showInfo(){return "AMD Ryzen7 3700X";}
};

#endif