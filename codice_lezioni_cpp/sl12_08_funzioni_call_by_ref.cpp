#include <iostream>
using namespace std;

void scambiaRef(int &a, int &b) {
	int temp;
	temp = a;
	a = b;
	b = temp;
}
int main() {
	int x = 7;
	int y = 5;
	cout << "scambio i valori x = " << x << " y = " << y << endl;
	cout << "passaggio per riferimento : ";
	scambiaRef(x,y);
	cout << "x = " << x << " y = " << y << endl;
}

