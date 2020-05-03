#ifndef DOCK_H
#define DOCK_H
#include "Ship.h"


class Dock
{
    private:
        int mHourIn;
        int mMinsIn;
        Ship* mShipPtr;

    public:
        // Constructors
        /*void*/ Dock() : mHourIn(0), mMinsIn(0), mShipPtr(nullptr) { }
        /*void*/ Dock(int hourIn, int minIn, Ship* shipPtr) : mHourIn(hourIn), mMinsIn(minIn), mShipPtr(shipPtr) { }
        /*void*/ Dock(const Dock& d) {mHourIn = d.mHourIn; mMinsIn = d.mMinsIn; mShipPtr = d.mShipPtr;}

        // Accessors
        int getHourIn() {return mHourIn;}
        int getMinutesIn() {return mMinsIn;}
        Ship* getShipPtr() {return mShipPtr;}

        // Mutators
        void setHourIn(int hr) {mHourIn = hr;}
        void setMinsIn(int mins) {mMinsIn = mins;}
        void setShipPtr(Ship *ptr) {mShipPtr = ptr;}
};

#endif // DOCK_H

