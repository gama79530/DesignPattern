#ifndef GARAGE_HEADER_INCLUDED
#define GARAGE_HEADER_INCLUDED

#include <memory>
#include <vector>

using namespace std;

template<class T, class C>
class Iterator{
public:
    Iterator(C *container);
    bool hasNext();
    T next();

private:
    typedef typename vector<T>::iterator iter_type;
    iter_type it_begin;
    iter_type it_end;
};

template<class T>
class Container{
public:
    friend class Iterator<T, Container<T>>;
    void add(T &t);
    void add(T &&t);
    shared_ptr<Iterator<T, Container<T>>> createIterator();

private:
    vector<T> contents;
};

#endif