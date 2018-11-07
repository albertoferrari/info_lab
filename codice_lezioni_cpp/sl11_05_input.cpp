#include <iostream>
using namespace std;
int main() {
	string name;
	int age;
	cout << "Name and age?" << endl;
	cin >> name >> age;
	cout << "Hello, " << name << "." << endl;
	cout << "You're " << age << " years old." << endl;

	string fullName;
	cout << "Surname and Name: ";
	cin.ignore();	// ignores \n that cin >> str has lefted (if user pressed enter key)
	getline(cin,fullName);
	cout << "Bye " << fullName;

	return 0;
}
