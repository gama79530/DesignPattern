#include "src/header/taxi.h"

int main(){
    Taxi taxi;
    taxi.hailed();
    taxi.checkout();
    taxi.hailed();
    taxi.hailed();
    taxi.checkout();
    taxi.checkout();
    
    return 0;
}