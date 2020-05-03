#ifndef LINKEDLIST_H
#define LINKEDLIST_H
#include "Ship.h"

class LinkedList
{
    private:
        Ship *mHead;
    public:
        // Constructors
        /*void*/ LinkedList() {mHead = nullptr;}
        /*void*/ LinkedList(Ship *sp) {mHead = sp;}

        // Accessor
        Ship* getHead() {return mHead;}

        // Mutator
        void setFirstShipPtr(Ship *sp) {mHead = sp;}

        // Overloaded += operator
        void operator+=(Ship*);

        // Overloaded -- operator
        Ship* operator--();

};

#endif // LINKEDLIST_H
