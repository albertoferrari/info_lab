#include <iostream>
using namespace std;

double media(int v1, int v2);	// prototipo

int main() {
    int val1, val2;
    cout << "Inserire due valori interi separati da spazio ";
    cin >> val1 >> val2;
    cout << "la media aritmetica fra " << val1 << " e " << val2 
			<< " = " << media(val1,val2) << endl;
    return 0;
}

double media(int v1, int v2) {	// definizione
    double med;
    med = (v1 + v2) / 2.0;
    return med;
}

