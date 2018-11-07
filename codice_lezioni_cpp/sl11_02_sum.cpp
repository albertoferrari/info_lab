#include <iostream>
int main() {
  int integer1, integer2, sum; 				// declaration
  std::cout << "Enter first integer\n"; 	// prompt
  std::cin >> integer1; 					// read an integer
  std::cout << "Enter second integer\n"; 	// prompt
  std::cin >> integer2; 					// read an integer
  sum = integer1 + integer2; 				// assignment of sum
  std::cout << "Sum is " << sum << std::endl; // print sum
  return 0; 		// indicate that program ended successfully
}
