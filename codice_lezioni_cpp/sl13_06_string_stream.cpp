#include <iostream>
#include <sstream>

using namespace std;

int main() {
	/* Split a text into a sequence of strings */
	string text = "one:two::three";
	istringstream sstr{text};  // a stream view on a string
	for (string item; getline(sstr, item, ':');) {
		cout << "- " << item << endl;
	}
}
