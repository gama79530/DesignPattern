#include "header/garage.h"

template<class T, class C>
Iterator<T, C>::Iterator(C *container){
    it_begin = container->contents.begin();
    it_end = container->contents.end();
}

template<class T, class C>
bool Iterator<T, C>::hasNext(){
    return it_begin != it_end;
}


template<class T, class C>
T Iterator<T, C>::next(){
    return *(it_begin++);
}

template<class T>
void Container<T>::add(T &t){
    contents.push_back(t);
}

template<class T>
void Container<T>::add(T &&t){
    contents.push_back(t);
}

template<class T>
shared_ptr<Iterator<T, Container<T>>> Container<T>::createIterator(){
    return make_shared<Iterator<T, Container<T>>>(this);
}