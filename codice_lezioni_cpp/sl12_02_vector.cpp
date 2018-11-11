#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    vector<string> myVector;

    // push_back aggiunge un elemento alla fine del vector e lo ridimensiona
    myVector.push_back("el_1");
    myVector.push_back("el_2");
    myVector.push_back("el_3");
    myVector.push_back("el_4");
    
    // [index] accesso all'elemento di indice index
    myVector[1] = "el_002";

    vector<int> intVect(5,0);		// 5 elementi inizializzati a 0
    // e : vector (accesso sequenziale agli elementi di vector)
    for (auto e : intVect)
        cout << e << " ";
    cout << endl;
    
    // e : vector (accesso sequenziale agli elementi di vector)
    for (auto e : myVector)
        cout << e << " ";
    cout << endl;

    // [index] accede all'elemento di indice index
    // size restituisce il numero di elementi presenti
    for (unsigned i=0; i<myVector.size(); ++i)
        cout << myVector[i] << " ";
    cout << endl;

    // at(index) restituisce il valore dell'elemento di indice index
    for (unsigned i=0; i<myVector.size(); ++i)
        cout << myVector.at(i) << " ";
    cout << endl;

    // begin() restituisce il riferimento al primo elemento
    // insert(index_ref, value) inserisce value dopo l'elemento riferito
    myVector.insert(myVector.begin() +2,"el_5");
    // e : vector (accesso sequenziale agli elementi di vector)
    for (auto e : myVector)
        cout << e << " ";
    cout << endl;

    // erase(index_ref) elimina l'elemento riferito da index_ref
    myVector.erase(myVector.begin() +2);
    // e : vector (accesso sequenziale agli elementi di vector)
    for (auto e : myVector)
        cout << e << " ";
    cout << endl;

    // ricerca di un elemento
    // begin(myVector) riferimento al primo elemento
    // end(myVector) riferimento all'alemento dopo l'ultimo
    auto pos = find(begin(myVector), end(myVector), "el_2");
    if (pos != end(myVector)) {     // trovato
        myVector.erase(pos);
    }
    for (auto e : myVector)
        cout << e << " ";
    cout << endl;

    //assegnamento valori iniziali
    vector<string> lista;
    lista.assign(10, ""); // 10 stringhe vuote
    for (auto e : lista)
        cout << e << " - ";
    cout << endl;

    // empty() restituisce true se non sono presenti elementi
    // clear() elimina tutti gli elementi
    if (!myVector.empty())
    {
        cout << "sono presenti elementi -> li elimino" << endl;
        myVector.clear();
    }
    if (myVector.empty())
        cout << "non sono presenti elementi" << endl;

    return 0;
}
