#include <iostream>
#include <fstream>

using namespace std;

int main() {
	ifstream f_in{"divina.txt"};	//declare and open
	if (f_in.fail()) {
		cout << "file error" << endl;  
		return 1;
	}
	string whole_text;
	getline(f_in, whole_text, '\0');  // read whole file
	cout << whole_text;
	f_in.close();
	return 0;
}
