#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
    
    int sum = 0;
    int maxsum = 0;
    int maxsum2 = 0;
    int maxsum3 = 0;

    fstream data;

    data.open("input.txt",ios::in); //open a file to perform read operation using file object
   if (data.is_open()){ //checking whether the file is open
      string bd;
      while(getline(data, bd)){ //read data from file object and put it into string.
         cout << bd << " "; //print the data of the string

         if (bd == "") {
            printf("\n");
            if (sum>maxsum) {maxsum3=maxsum2; maxsum2=maxsum; maxsum=sum;}
            else if (sum>maxsum2 && sum<=maxsum) {maxsum3=maxsum2; maxsum2=sum;}
            else if (sum>maxsum3 && sum<=maxsum2) {maxsum3=sum;}
            index+=1;
            sum=0;
         } else {
            sum=sum+stoi(bd);
         }

      }
      cout<<"\nThe max sum is: "<<maxsum;
      cout<<"\nThe three max sums are: "<<maxsum<<" "<<maxsum2<<" "<<maxsum3<<"\n"<<"The total sum is: "<<maxsum+maxsum2+maxsum3<<"\n";
      }

    return 0;
}
