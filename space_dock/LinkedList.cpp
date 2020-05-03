#include "LinkedList.h"
#include "Ship.h"

void LinkedList::operator+=(Ship *sp) // sp is pointer to new node/ship
{
    if (!mHead){
        mHead = sp;
    } else {
        Ship *ptr = mHead;
        while (ptr){
            if (ptr->getShip() == nullptr){
                ptr->setNextShip(sp);
                break;
            } else{
                ptr = ptr->getShip();
            }
        }
    }
}

Ship* LinkedList::operator--()
{
    Ship *sp = mHead;
    mHead = mHead->getShip();
    return sp;
}
