#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {

    fstream input;
    input.open("input.txt", ios::in);

    if (input.is_open()) {
        string linje;
        string b;
        string s;


        int size = 0;
        int sum1 = 0;
        int sum2 = 0;
        string x1;
        string x2;
        string y1;
        string y2;

        int smallest_interval1;
        int smallest_interval2;
        int largest_interval1;
        int largest_interval2;

        while (getline(input,linje)) {
            size = linje.size();
            
            b=linje.substr(0,linje.find_first_of(","));
            s=linje.substr(linje.find_first_of(",")+1,size);
            
            x1=b.substr(0,b.find_first_of("-"));
            x2=b.substr(b.find_first_of("-")+1,b.size());

            y1=s.substr(0,s.find_first_of("-"));
            y2=s.substr(s.find_first_of("-")+1,s.size());

            if (stoi(x2)-stoi(x1) < stoi(y2)-stoi(y1)) {
                smallest_interval1 = stoi(x1);
                smallest_interval2 = stoi(x2);
                largest_interval1 = stoi(y1);
                largest_interval2 = stoi(y2);
            } else {
                smallest_interval1 = stoi(y1);
                smallest_interval2 = stoi(y2);
                largest_interval1 = stoi(x1);
                largest_interval2 = stoi(x2);
            }

            if (smallest_interval1>=largest_interval1 && smallest_interval2<=largest_interval2) {
                sum1+=1;
            }
            if (((smallest_interval1>=largest_interval1) && (smallest_interval1<=largest_interval2)) || ((smallest_interval2<=largest_interval2) && (smallest_interval2>=largest_interval1))) {
                sum2+=1;
            }
        }
        cout<<"The amount of pairs that absorb each other is: "<<sum1<<"\n";
        cout<<"The amount of pairs that overlap each other is: "<<sum2<<"\n";


    }
}