/*
 chiede all'utente il valore del raggio r di un cerchio
 mostra il valore dell'area e della circonferenza
 se r è negativo, però, mostra un messaggio d'errore
*/

#include <iostream>
#include <cmath>

using namespace std;

int main() 
{
	const double pi = 3.1415926535897;
	double raggio;
	cout << "raggio: ";
	cin >> raggio;
	if (raggio < 0)
	{
		cout << "raggio negativo!" << endl;
	}
	else
	{
		double circonf = 2 * pi * raggio;
		double area = pi * pow(raggio,2);
		cout << "circonferenza " << circonf << endl;
		cout << "area " << area << endl;
    }
}
