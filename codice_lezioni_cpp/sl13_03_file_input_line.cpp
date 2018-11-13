#include <iostream>
#include <fstream>

using namespace std;

int main() {
	ifstream f_in{"divina.txt"};	//declare and open
	if (f_in.fail()) {
		cout << "file error" << endl;  
	 return 1;
	}
	// for each line in f_in...
	for (string line; getline(f_in, line);) {
		cout << line << endl;
	}
	f_in.close();
	return 0;
}
