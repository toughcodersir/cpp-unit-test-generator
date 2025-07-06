#include <iostream>
#include <climits>
#include <cassert>
#include "../functions.h"  // ✅ Include your header file

int main() {
    // Basic Addition
    assert(add(5, 3) == 8);
    // Basic Subtraction
    assert(subtract(5, 3) == 2);
    // Negative Addition
    assert(add(-5, -3) == -8);
    // Negative Subtraction
    assert(subtract(-5, -3) == 2);
    // Edge Case: Subtracting INT_MIN from INT_MIN
    assert(subtract(INT_MIN, INT_MIN) == 0);
    
    std::cout << "✅ All tests passed!" << std::endl;
    return 0;
}
