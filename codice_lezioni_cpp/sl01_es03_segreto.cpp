/*
 genera un numero “segreto” a caso tra 1 e 90
 chiede ripetutamente all'utente di immettere un numero
 finché non indovina quello generato
 ad ogni tentativo, dice se il numero immesso
 è maggiore o minore del numero segreto
*/

#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() 
{
	int n,val;
	srand(time(nullptr));
	n = rand() % 90 + 1;
	cout << n << endl;		//debug
	cout << "inserisci un numero [1..90] ";
	cin >> val;
	while (val!=n)
	{
		if (val < n)
			cout << "e' minore del numero segreto" << endl;
		else
			cout << "e' maggiore del numero segreto" << endl;
		cout << "inserisci un numero [1..90] ";
		cin >> val;
	} 
	cout << "hai indovinato! Il numero segreto e' " << n; 
}
