/*
 dati di input: capitale iniziale, tasso d'interesse, durata investimento (anni)
 calcola il capitale dopo ogni anno
*/

#include <iostream>

using namespace std;

int main() 
{
	float capitale, tasso, anni;
	cout << "capitale tasso anni ";
	cin >> capitale >> tasso >> anni;
	for (int anno=1; anno<=anni; anno++) {
		capitale = capitale + capitale * tasso / 100;
		cout << "anno: " << anno << " capitale: " << capitale << endl; 
	}
}
