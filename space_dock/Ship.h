#ifndef SHIP_H
#define SHIP_H
#include <string>

class Ship
{
    private:
        std::string mName;
        std::string mID;
        int mCredit;
        Ship *mNextShip;

    public:
        // Constructors
        /*void*/ Ship() : mName(""), mID(""), mCredit(0), mNextShip(nullptr) { }
        /*void*/ Ship(std::string name, std::string ID, int credit, Ship *sp) : mName(name), mID(ID), mCredit(credit), mNextShip(sp) { }
        /*void*/ Ship(const Ship &sp) {mName = sp.mName; mID = sp.mID; mCredit = sp.mCredit; mNextShip = sp.mNextShip;}


        // Accessors
        std::string getName() {return mName;}
        std::string getID() {return mID;}
        int getCredit() {return mCredit;}
        Ship* getShip() {return mNextShip;}

        //Mutators
        void setName(std::string n) {mName = n;}
        void setID(std::string id) {mID = id;}
        void setCredit(int c) {mCredit = c;}
        void setNextShip(Ship *next) {mNextShip = next;}

};

#endif // SHIP_H
