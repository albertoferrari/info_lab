#include <iostream>
using std::cout; 	// program uses cout
using std::cin; 	// program uses cin
using std::endl; 	// program uses endl
int main() {
  int integer1, integer2, sum; 				// declaration
  cout << "Enter first integer\n"; 			// prompt
  cin >> integer1; 							// read an integer
  cout << "Enter second integer\n"; 		// prompt
  cin >> integer2; 							// read an integer
  sum = integer1 + integer2;  				// assignment of sum
  cout << "Sum is " << sum << std::endl; 	// print sum
  return 0; 		// indicate that program ended successfully
}
