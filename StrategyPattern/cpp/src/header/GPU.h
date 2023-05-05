#ifndef GPU_HEADER_INCLUDED
#define GPU_HEADER_INCLUDED

#include <string>

using namespace std;

class GPU{
public:
    virtual string showInfo() = 0;
};

class NVIDIA_GeForce_GTX_1660_SUPER: public GPU{
public:
    string showInfo(){return "NVIDIA GeForce GTX 1660 SUPER";}
};

#endif