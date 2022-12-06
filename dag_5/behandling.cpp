#include <iostream>
#include <fstream>
#include <string>
#include "behandling.hpp"
#include <vector>


using namespace std;

/*
vector<char> one = {'Q','G','P','R','L','C','T','F'};
vector<char> two = {'J','S','F','R','W','H','Q','N'};
vector<char> three = {'Q','M','P','W','H','B','F'};
vector<char> four = {'F','D','T','S','V'};
vector<char> five = {'Z','F','V','W','D','L','Q'};
vector<char> six = {'S','L','C','V'};
vector<char> seven = {'F','D','V','M','B','Z'};
vector<char> eight = {'J','S','F','R','W','H','Q','N'};
*/

vector<char> one;
vector<char> two;
vector<char> three;
vector<char> four;
vector<char> five;
vector<char> six;
vector<char> seven;
vector<char> eight;

void stack2::push(char input) {
    bogstav.push_back(input);
}

void push(vector<char> liste, char input) {
    liste.push_back(input);
}

char stack2::pop() {
    char return_value = bogstav.back();
    bogstav.pop_back();

    return return_value;
}


int main() {

    fstream input;
    stack2 test;

    input.open("stack.txt",ios::in);

    if (input.is_open()) {
        string linje;
        while (getline(input,linje)) {

        for (int i=0;i<=linje.size();i=i+2) {
            push(one,linje[i]);
        }
        cout<<one.back();
        }
    }
}

