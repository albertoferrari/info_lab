#include <iostream>
#include "Ball.h"

using namespace std;

int main()
{
    Ball b1{40, 80};
    Ball b2{80, 40};

    for (auto i = 0; i < 25; ++i)
    {
        b1.move();
        b2.move();
        cout << b1.get_x() << ", " << b1.get_y() << endl;
        cout << b2.get_x() << ", " << b2.get_y() << endl << endl;
    }
}
