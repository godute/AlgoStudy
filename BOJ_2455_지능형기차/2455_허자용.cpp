#include <iostream>

using namespace std;

// meaningless line

int main() {
	int hopon, hopoff;
    int max_n = 0;
    int current = 0;
	for (int i = 0; i < 4; i++) {
		cin >> hopoff >> hopon;
		current += hopon - hopoff;
        if (max_n < current) max_n = current;
	}

	cout << max_n << endl;
	return 0;
}