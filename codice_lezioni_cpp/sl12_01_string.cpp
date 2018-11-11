#include <iostream>
#include <string>
using namespace std;
int main() {
	string s1,s2,s3;
	s1 = "Informatica";
	s2 = s1 + " e laboratorio " + "di programmazione";
	// error: invalid operands of types '...' and '...' to binary 'operator+'
	// s3 = "Informatica" + " e laboratorio";
	s2[0] = 'i';		// sostituzione del primo carattere della stringa
	cout << "contenuto della stringa s2: " << s2 << endl;
	cout << "numero di caratteri della stringa s2: " << s2.length() << endl;
	s3 = "Ingegneria dei Sistemi Informativi";
	int pos;
	pos = s3.find("In");
	cout << "nella stinga " << s3 << endl << "la sottostringa " << "In" 
	     << " si trova in posizione " << pos << endl;
	pos = s3.find("out");
	cout << "nella stinga " << s3 << endl << "la sottostringa " << "out" 
	     << " si trova in posizione " << pos << endl;	
	cout << s3.substr(15,7) << endl;          
    return 0;
}
