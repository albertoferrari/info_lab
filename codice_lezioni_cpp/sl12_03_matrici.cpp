// constructing vectors
#include <iostream>
#include <vector>

using namespace std;

int main ()
{
	// matrice inizializzata
	vector<vector<int>> matrice = { {2, 4, 3, 8},
								   {9, 3, 2, 7},
								   {5, 6, 9, 1} };
								   	
	auto righe_m = matrice.size();		// numero di righe	
	auto colonne_m = matrice[0].size();	// numero di colonne
	
	for (auto r = 0; r < righe_m; ++r) {
		for (auto c = 0; c < colonne_m; ++c) {
			cout << matrice[r][c] << " ";
		}
		cout << endl;
	}
	
	auto righe_v = 6;
	auto colonne_v = 8;
	vector <vector<int> > vuota(righe_v, vector<int>(colonne_v));
	for (auto r = 0; r < righe_v; ++r) {
		for (auto c = 0; c < colonne_v; ++c) {
			cout << vuota[r][c] << " ";
		}
		cout << endl;
	}

	auto righe_c = 3;
	auto colonne_c = 4;
	vector<vector<char>> matrice_car;
	matrice_car.assign(righe_c, vector<char>(colonne_c, '-'));
	for (unsigned r = 0; r < matrice_car.size(); ++r) {
		for (unsigned c = 0; c < matrice_car[0].size(); ++c) {
			cout << matrice_car[r][c] << " ";
		}
		cout << endl;
	}
  return 0;
}
