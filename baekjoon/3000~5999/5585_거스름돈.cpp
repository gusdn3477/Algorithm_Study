#include <iostream>
#include <string>
#include <map>
using namespace std;

int main(void) {

	cin.tie(0);
	cin.sync_with_stdio(false);

	int money;
	int change;
	int count = 0;

	cin >> money;

	change = 1000 - money;
	if (change / 500) {
		count += change / 500;
		change = change % 500;
	}

	if (change / 100) {
		count += change / 100;
		change = change % 100;
	}

	if (change / 50) {
		count += change / 50;
		change = change % 50;
	}

	if (change / 10) {
		count += change / 10;
		change = change % 10;
	}

	if (change / 5) {
		count += change / 5;
		change = change % 5;
	}

	if (change / 1) {
		count += change / 1;
	}

	cout << count;


	return 0;
}