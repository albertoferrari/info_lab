/*
 genera e stampa tre numeri interi casuali: a, b, c
 ciascuno compreso tra 1 e 6
 determina e mostra qual è il minore dei tre
*/

#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() 
{
	int a,b,c;
	srand(time(nullptr));
	a = rand() % 6 + 1;
	b = rand() % 6 + 1;
	c = rand() % 6 + 1;
	cout << "a=" << a << " b=" << b << " c=" << c << endl;
	cout << "minore: ";
	if (a<b && a<c)
		cout << a;
	else if (b<c)
		cout << b;
	else
		cout << c;
}
