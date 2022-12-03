#include <iostream>
#include <string>
#include <fstream>
using namespace std;

char samme(string linje, string half1, string half2) {
	//int antal=0;
	char duplicate;

	sort(linje.begin(),linje.end());

	for (int i=0;i<linje.size();i++) {
		if (linje[i]==linje[i+1] && (half1.find(linje[i])!= std::string::npos) && (half2.find(linje[i])!= std::string::npos)) {
			//antal+=1
			duplicate=linje[i];
		}
	}
	return duplicate;
}

int char_to_value(char bogstav) {
	if (isupper(bogstav)) {
		bogstav = tolower(bogstav);
		int tal = (int)bogstav-96+26;
		return tal;	

	} else {
		int tal = (int)bogstav-96;
		return tal;	
	}
};

int find_max_length(int one, int two, int three) {
	if (one>two) {
		if (one>three) {
			return one;
		} else {
			return three;
		}
	} else if (two>one) {
		if (two>three) {
			return two;
		} else {
			return three;
		}
	} else {
		if (three>two) {
			return three;
		} else {
			return two;
		}
	}
	}

int main () {

	//Del 1;
	fstream input;
	string half1;
	string half2;
	char duplicate;
	int sum = 0;

	input.open("input.txt",ios::in);
	if (input.is_open()) {
		string linje;	
		while (getline(input,linje)) {
			half1=linje.substr(0,(linje.size()/2));					
			half2=linje.substr((linje.size()/2),linje.size());
			duplicate = samme(linje,half1,half2);

			sum += char_to_value(duplicate);
		}
	}
	cout<<"The sum is: "<<sum<<"\n";


	//Del 2;
	fstream input2;
	sum = 0;

	int length1;
	int length2;
	int length3;
	bool found=false;

	input2.open("input.txt",ios::in);
	if (input2.is_open()) {
		string linje;
		string nylinje;
		int counter = 0;	
		while (getline(input2,linje)) {
			if (counter==0) {
				length1=linje.size();
				nylinje=linje;
				counter++;
			} else if (counter==1) {
				length2=linje.size();
				nylinje+=linje;
				counter++;
			} else if (counter==2) {
				length3=linje.size();
				nylinje+=linje;
				counter++;
			} 
			
			if (counter==3) {
				
				for (int i =0;i<find_max_length(length1,length2,length3) && found==false; i++) {
					for (int j =0;j<find_max_length(length1,length2,length3) && found==false; j++) {
						for (int k =0;k<find_max_length(length1,length2,length3) && found==false; k++) {
					
							if (nylinje[i]==nylinje[j+length1] && nylinje[i]==nylinje[k+length2] && found==false) {
								duplicate=nylinje[i];
								sum+=char_to_value(duplicate);
								found=true;
							}
						}
					}
				}
				nylinje="";
				counter=0;
				found=false;
			}
		}
	}
	cout<<"The sum is: "<<sum<<"\n";


}