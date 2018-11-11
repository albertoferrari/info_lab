#include <iostream>
#include <vector>

using namespace std;

/**
 * Restituisce lista (vector) di valori in input 
 * */
vector<int> leggi()
{
	vector<int> v;
	int val;
	cout << "valore: (0 termina)"; cin >> val;
	while (val != 0) 
	{
		v.push_back(val);
		cout << "valore: (0 termina)"; cin >> val;
	}
	return v;
}

void raddoppia(vector<int> &v)
{
	for (unsigned i=0; i<v.size(); ++i)
		v[i] = 2*v[i];
}

void stampa(vector<int> v)
{
	for(auto e : v)
		cout << e << " ";
	cout << endl;
}

int main( ) {
    vector<int> valori;
    valori = leggi();
    stampa(valori);
    raddoppia(valori);
    stampa(valori);
    return 0;
}


