#include "Ship.h"
#include "Dock.h"
#include "Ticket.h"
#include "LinkedList.h"
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

#define NUM_DOCK 10

// Test program
int main()
{
    // Create a linked list
    LinkedList LL;
    // Create dock array
    Dock D[NUM_DOCK];

    ofstream ofile ("Tickets.txt");
    if (!ofile.is_open()){
        std::cout << "Unable to open file to write" << std::endl;
        return -1;
    }
    ofile.close();

    string filename;
    cin >> filename;
    // read from files
    std::string line;
    //ifstream ifile("sample_Knowhere.dat");
    ifstream ifile(filename);
    if (!ifile.is_open()){
        std::cout << "Unable to open file to read" << std::endl;
        return -1;
    }
    while (getline(ifile, line)){
        // tokenize line
        vector<string> tokens;
        size_t pos = 0;
        while((pos = line.find(' ')) != std::string::npos){
            tokens.push_back(line.substr(0, pos));
            line.erase(0, pos + 1);
        }
        tokens.push_back(line);

        std::string cmd, time_str, ship_name, ship_id;
        int credit = 0, ship_hour = 0, ship_min = 0;
        if (tokens.size() == 5){
            cmd = tokens[0];
            time_str = tokens[1];
            ship_name = tokens[2];
            ship_id = tokens[3];
            credit = std::stoi(tokens[4]);
        } else if (tokens.size() == 3) {
            cmd = tokens[0];
            ship_id = tokens[1];
            time_str = tokens[2];
        } else{
            std::cout << "Unexpected input" << std::endl;
            return -1;
        }

        tokens.clear();
        pos = 0;
        while((pos = time_str.find(':')) != std::string::npos){
            tokens.push_back(time_str.substr(0, pos + 1));
            time_str.erase(0, pos + 1);
        }
        tokens.push_back(time_str);
        ship_hour = std::stoi(tokens[0]);
        ship_min = std::stoi(tokens[1]);

        if (cmd == std::string("enter")){
            // Create dynamic ship objects
            // Add ships to Linked List using overloaded += operator
            Ship *S = new Ship(ship_name, ship_id, credit, nullptr);
            printf("%s enters %02d:%02d\n", ship_id.c_str(), ship_hour, ship_min);

            bool fullDocks = true;
            for (int i = 0; i < NUM_DOCK; i++){
                if (D[i].getShipPtr() == nullptr){
                    // Connect the dock to the ship that was removed
                    D[i].setShipPtr(S);
                    // Update dock time in
                    D[i].setHourIn(ship_hour);
                    D[i].setMinsIn(ship_min);

                    fullDocks = false;
                    break;
                }
            }
            if (fullDocks) {
                LL += S;
            }
        } else if  (cmd == std::string("exit")){
            for (int i = 0; i < NUM_DOCK; i++){
                if (D[i].getShipPtr() && D[i].getShipPtr()->getID() == ship_id){
                    Ship *S = D[i].getShipPtr();
                    printf("%s exits %02d:%02d\n", ship_id.c_str(), ship_hour, ship_min);

                    // Create ticket object
                    Ticket T(S, &D[i], ship_hour, ship_min);
                    // Disconnect ship from the dock
                    D[i].setShipPtr(nullptr);

                    // Display ticket object using overloaded << operator
                    if (T.calculateFine() > 0){
                        ofstream ofile ("Tickets.txt", ios::app);
                        if (!ofile.is_open()){
                            std::cout << "Unable to open file to write" << std::endl;
                            return -1;
                        }
                        ofile << T << endl;
                        ofile.close();
                    }
                    break;
                }
            }
        }
    }
    ifile.close();

    return 0;
}
