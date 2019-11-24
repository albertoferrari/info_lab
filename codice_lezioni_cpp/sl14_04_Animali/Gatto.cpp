#include <string>
#include <iostream>
#include "Animale.cpp"

using namespace std;

class Gatto : public Animale
{
public:
	Gatto(int a, int p ): Animale(a, p) { }
	void visualizza() const {
		cout << "Sono un gatto ";
		Animale::visualizza();
	}

private:
};


