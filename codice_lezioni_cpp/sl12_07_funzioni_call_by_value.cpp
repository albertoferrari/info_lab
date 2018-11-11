#include <iostream>
using namespace std;

void scambiaVal(int a, int b) {
	int temp;
	temp = a;
	a = b;
	b= temp;
}

int main() {
	int x,y; x = 7; y = 5;
	cout << "scambio i valori x = " << x << " y = " << y << endl;
	cout << "passaggio per valore : ";
	scambiaVal(x,y);
	cout << "x = " << x << " y = " << y << endl;
    return 0;
}
