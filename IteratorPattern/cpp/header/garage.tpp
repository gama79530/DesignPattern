#include <memory>
#include <vector>

template <class T>
class Iterator
{
public:
    Iterator(Garage<T> *garage)
    {
        it_begin = garage->contents.begin();
        it_end = garage->contents.end();
    }

    bool hasNext()
    {
        return it_begin != it_end;
    }

    T next()
    {
        return *(it_begin++);
    }

private:
    typename std::vector<T>::iterator it_begin;
    typename std::vector<T>::iterator it_end;
};

template <class T>
class Garage
{
public:
    friend class Iterator<T>;

    void add(T &t)
    {
        contents.push_back(t);
    }

    void add(T &&t)
    {
        contents.push_back(move(t));
    }

    std::shared_ptr<Iterator<T>> createIterator()
    {
        return std::make_shared<Iterator<T>>(this);
    }

private:
    std::vector<T> contents;
};