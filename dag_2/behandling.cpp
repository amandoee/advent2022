#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {

    fstream data;
    string elf ="";
    string me ="";

    int wins = 0;
    int losses = 0;
    int draws = 0;

    int total_points = 0;

    data.open("inputv2.txt",ios::in); //open a file to perform read operation using file object
      if (data.is_open()){ //checking whether the file is open
         string alle_numre;
         while(getline(data, alle_numre)){ //read data from file object and put it into string.

            elf="";
            me="";


            cout << alle_numre << "\n"; //print the data of the string
               while (alle_numre!="") {
                if (alle_numre.find_first_of(",")==1 || alle_numre.find_first_of(" ")==1) {

                    if (elf=="") {
                        elf = alle_numre.substr(0,1);
                        alle_numre.erase(0,2);
                    } else {
                        me = alle_numre.substr(0,1);
                        alle_numre.erase(0,2);
                    }
                }
                else {
                    alle_numre.erase(0,1);
                }
            }

            if (elf=="A") {
                if (me=="X") {
                    draws+=1;
                    total_points+=3;
                    total_points+=1;
                } else if (me=="Y") {
                    wins+=1;
                    total_points+=6;
                    total_points+=2;
                } else if (me=="Z") {
                    total_points+=3;
                    losses+=1;
                }}
            else if (elf=="B") {
                if (me=="X") {
                    losses+=1;
                    total_points+=1;
                } else if (me=="Y") {
                    draws+=1;
                    total_points+=3;
                    total_points+=2;
                } else if (me=="Z") {
                    wins+=1;
                    total_points+=6;
                    total_points+=3;
                }}
            else if (elf=="C") {
                if (me=="X") {
                    wins+=1;
                    total_points+=6;
                    total_points+=1;
                } else if (me=="Y") {
                    losses+=1;
                    total_points+=2;
                } else if (me=="Z") {
                    draws+=1;
                    total_points+=3;
                    total_points+=3;
                }
            }
            }




            }
        cout<<"The amount of W: "<<wins<<" L: "<<losses<<" D:"<<draws<<"\n";
        cout<<"The totoal amount of points is: "<<total_points<<"\n";

        wins=0;
        losses=0;
        draws=0;
        total_points=0;

        int rock = 1;
        int paper = 2;
        int scissors = 3;

        fstream del2;
        del2.open("inputv2.txt",ios::in); //open a file to perform read operation using file object
      if (del2.is_open()){ //checking whether the file is open
         string alle_numre;
         while(getline(del2, alle_numre)){ //read data from file object and put it into string.

            elf="";
            me="";

               while (alle_numre!="") {
                if (alle_numre.find_first_of(",")==1 || alle_numre.find_first_of(" ")==1) {

                    if (elf=="") {
                        elf = alle_numre.substr(0,1);
                        alle_numre.erase(0,2);
                    } else {
                        me = alle_numre.substr(0,1);
                        alle_numre.erase(0,2);
                    }
                }
                else {
                    alle_numre.erase(0,1);
                }
            }

            if (elf=="A") {
                if (me=="X") {
                    losses+=1;
                    total_points+=scissors;

                } else if (me=="Y") {
                    draws+=1;
                    total_points+=rock;

                } else if (me=="Z") {
                    wins+=1;
                    total_points+=paper;
                }}
            else if (elf=="B") {
                if (me=="X") {
                    losses+=1;
                    total_points+=rock;

                } else if (me=="Y") {
                    draws+=1;
                    total_points+=paper;
                    
                } else if (me=="Z") {
                    wins+=1;
                    total_points+=scissors;
                }}
            else if (elf=="C") {
                if (me=="X") {
                    losses+=1;
                    total_points+=paper;
                    
                } else if (me=="Y") {
                    draws+=1;
                    total_points+=scissors;
                } else if (me=="Z") {
                    wins+=1;
                    total_points+=rock;
                }
            }
            }
            total_points+=wins*6+draws*3;

            cout<<"The total amount of points after Part Two is: "<<total_points<<"\n";




            }


}
