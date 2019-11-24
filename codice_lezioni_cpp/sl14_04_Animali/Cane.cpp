#include <string>
#include <iostream>
#include "Animale.cpp"

using namespace std;

class Cane : public Animale {
public:
	Cane(int a = 0, int p = 0, string nome="Pluto"): Animale(a, p) { 
		setNome( nome );
	}
	string getNome() { return nome; }
	void setNome(string val) { nome=val; }
	void visualizza() const {
		cout << "Sono un cane di nome: "  << nome ;
		Animale::visualizza();
	}
private:
	string nome;
};

