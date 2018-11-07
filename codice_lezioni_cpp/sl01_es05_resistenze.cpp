/*
 legge, attraverso un ciclo, una sequenza di valori di resistenze elettriche
 la sequenza termina quando l'utente immette il valore 0
 alla fine, visualizza la resistenza equivalente,
 sia nel caso di resistenze disposte in serie, che in parallelo
*/

#include <iostream>

using namespace std;

int main() 
{
	double serie = 0, parallelo = 0, res;
	cout << "valore resistenza (0 per terminare) ";
	cin >> res;
	while (res != 0)
	{
		serie += res;
		parallelo += 1/res;
		cout << "valore resistenza (0 per terminare) ";
		cin >> res;
	}
	cout << "serie: " << serie << endl;
	cout << "parallelo: " << 1/parallelo << endl;
}
