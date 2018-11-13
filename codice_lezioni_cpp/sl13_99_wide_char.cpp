#include <fstream>

using namespace std;

int main()
{
	// wofstream output stream class to operate on files using wide characters
    wofstream f_out("myfile.txt");
    f_out << "àèìòù" << endl;
    f_out.close();
}
