#include <iostream>
#include <fstream>

using namespace std;

int main() {
   string s;
   ifstream f_in;	
   f_in.open("divina.txt");
   if (f_in.fail()) {
     cout << "file error" << endl;  
     return 1;
   }
   f_in >> s;
   while(!f_in.eof()) {
     cout << s << endl;
     f_in >> s;
   }
   f_in.close();
   return 0;
}
