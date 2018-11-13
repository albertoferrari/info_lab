#include <iostream>
#include <fstream>
using namespace std;
int main() {
   fstream f1,f2;
   int r; char p,c;
   f1.open("temp.txt", ios::out);
   f1 << 'k' << 'e' << 1 << endl;
   f1 << 'Q' << 'd' << 8 << endl;
   f1.close();
   f2.open("temp.txt", ios::in);
   f2 >> p;
   while(!f2.eof()) {
     cout << p << "(";
     f2 >> c;
     cout << c << ",";
     f2 >> r;
     cout << r << ")" << endl;
     f2 >> p;
   }
   f2.close();	
}
