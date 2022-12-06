#include <vector>
using namespace std;
//Lav en stack som linked list

class stack2 {
public:
    void push(char bogstav);
    char pop();
    
private:
    vector<char> bogstav;

};