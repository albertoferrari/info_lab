#include <iostream>
#include <fstream>

using namespace std;

int main() {
   ofstream f_out;						// output stream
   f_out.open("myfile.txt");			// open
   f_out << "first line" << endl;		// write
   f_out << "second line" << endl;
   f_out.close();						//
   return 0;
}
