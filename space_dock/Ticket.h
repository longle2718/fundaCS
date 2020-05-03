#ifndef TICKET_H
#define TICKET_H
#include "Ship.h"
#include "Dock.h"
#include <iostream>

class Ticket
{
    private:
        Ship *mShipPtr;
        Dock *mDockPtr;
        int   mHourOut;
        int   mMinsOut;
    public:
        // Constructors
        /*void*/ Ticket() : mShipPtr(nullptr), mDockPtr(nullptr), mHourOut(0), mMinsOut(0) { }
        /*void*/ Ticket(Ship* shipPtr, Dock* dockPtr, int hourOut, int minsOut) :
            mShipPtr(shipPtr), mDockPtr(dockPtr), mHourOut(hourOut), mMinsOut(minsOut) { }
        /*void*/ Ticket(const Ticket& t) {mShipPtr = t.mShipPtr; mShipPtr = t.mShipPtr; mShipPtr = t.mShipPtr; mShipPtr = t.mShipPtr;} // copy constructor

        // Accessors
        Ship *getShipPtr() {return mShipPtr;}
        Dock *getDockPtr() {return mDockPtr;}
        int getHourOut() {return mHourOut;}
        int getMinsOut() {return mMinsOut;}

        // Mutators
        void setShipPtr(Ship *sp) {mShipPtr = sp;}
        void setDockPtr(Dock *dp) {mDockPtr = dp;}
        void setHourOut(int hr) {mHourOut = hr;}
        void setMinsOut(int mins) {mMinsOut = mins;}

        int calDuration(){
            return (mHourOut - mDockPtr->getHourIn())*60 + (mMinsOut - mDockPtr->getMinutesIn());
        }

        // Calculate fine function
        int calculateFine(){
            int duration = calDuration();
            int fine_min = duration - mShipPtr->getCredit();
            int fine_unit = fine_min > 60 ? 200 * 60 + (fine_min - 60) * 500 : std::max(0, 200 * fine_min);
            return fine_unit;
        }

        // Overloaded << operator
        friend std::ostream& operator<<(std::ostream& os, Ticket &t){
            char tIn [100];
            sprintf(tIn, "%2d:%02d", t.mDockPtr->getHourIn(), t.mDockPtr->getMinutesIn());
            char tOut [100];
            sprintf(tOut, "%2d:%02d", t.mHourOut, t.mMinsOut);
            return os   << "Ship ID: " << t.mShipPtr->getID() << std::endl
                        << "Name: " << t.mShipPtr->getName() << std::endl
                        << "Time In: " << tIn << std::endl
                        << "Time Out: " << tOut << std::endl
                        << "Credited Minutes: " << t.mShipPtr->getCredit() << std::endl
                        << "Extra Minutes: " << std::max(0, t.calDuration() - t.mShipPtr->getCredit()) << std::endl
                        << "Fine: " << t.calculateFine() << " units" << std::endl;
        };

};

#endif // TICKET_H
