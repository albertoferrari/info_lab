#include <iostream> 
#include <cmath> 

using namespace std;
int main() {
	double y, x = 5.22;
	// la funzione pow ha prototipo double pow( double, double)
	// y = pow("x", 3.0); // error: no matching function 
				// for call to 'pow(const char [2], double)'
	// y = pow(x + 3.0); // error: no matching function for call to 'pow(double)'
	y = pow(x, 3.0); 	// ok!
	y = pow(x, 3); 	// ok! Il compilatore converte l'intero 3 in double
	cout << x << " elevato al cubo vale: " << y << endl;
	return 0;
}

