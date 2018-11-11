#include <cmath>
#include <iostream>
using namespace std;

double ipotenusa(double a, double b) 
{
    auto c = sqrt(a * a + b * b);
    return c;
}

void stampa_ip(double ip)
{
    cout << "ipotenusa: " << ip << endl;
}

int main() 
{
    auto l1 = 3.0, l2 = 4.0;
    auto l3 = ipotenusa(l1, l2);
    stampa_ip(l3);
}
