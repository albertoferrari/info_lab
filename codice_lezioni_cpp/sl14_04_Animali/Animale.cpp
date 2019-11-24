#include <iostream>
using namespace std;

class Animale {
public:
	Animale(int a, int p): altezza(a), peso(p) {};
	int getAltezza() { return altezza; }
	void setAltezza(int val) {altezza=val;}
	int getPeso() { return peso; }
	void setPeso(int val) { peso = val; }
	void visualizza() const {
		cout << "altezza " << altezza  << " peso " << peso << endl;
	}
private:
	int altezza;
	int peso;
};
