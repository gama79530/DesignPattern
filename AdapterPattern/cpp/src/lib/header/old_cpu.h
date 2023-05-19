#ifndef OLD_CPU_HEADER_INCLUDED
#define OLD_CPU_HEADER_INCLUDED

#include <string>

using namespace std;

class Old_CPU{
public:
    virtual string getName() = 0;
};

class Pentium4: public Old_CPU{
public:
    string getName();
};

#endif