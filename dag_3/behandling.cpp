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
		cout<<"The sum is: "<<sum<<"\n";

	int length1;
	int length2;
	int length3;

	input2.open("input.txt",ios::in);
	if (input2.is_open()) {
		string linje;
		string nylinje;

		string linje1;
		string linje2;
		string linje3;
		string what;

		string biggest_linje;
		bool found= false;



		int counter = 0;	
		while (getline(input2,linje)) {
			if (counter==0) {
				length1=linje.size();
				nylinje=linje;
				linje1 = linje;

				counter++;
			} else if (counter==1) {
				length2=linje.size();
				linje2=linje;
				nylinje+=linje;
				counter++;
			} else if (counter==2) {
				length3=linje.size();
				nylinje+=linje;
				linje3=linje;
				counter++;
			} 
			
			if (counter==3) {
				
				if (find_max_length(length1,length2,length3)==length1) {
						biggest_linje=linje1;
					} else if (find_max_length(length1,length2,length3)==length2) {
						biggest_linje=linje2;
					} else {
						biggest_linje=linje3;
					}

				for (int i =0;i<(biggest_linje.size()); i++) {
				//Check om linjer er npos eller ej.	
				
					if (found==false && linje1.find(biggest_linje[i])!=std::string::npos && linje2.find(biggest_linje[i])!=std::string::npos && linje3.find(biggest_linje[i])!=std::string::npos) {
						//if statement er forkert. Finder 'r' i 2. omgang, ved 5. linje.
						duplicate = biggest_linje[i];
						sum += char_to_value(duplicate);
						
						found=true;
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