#include <iostream>
#include <vector>

using namespace std;

int main(void) {

	cin.sync_with_stdio(false);
	cin.tie(0);
	
	vector<int> v;
	int N,M;
	int count, gap;
	cin >> N >> M;

	gap = 0;
	for (int i = 0; i < N; i++) {
		cin >> count;
		v.push_back(count);
	}

	for (int i = 0; i < N - 2; i++) {
		for (int j = i + 1; j < N - 1; j++) {
			for (int z = j + 1; z < N; z++) {
				if (v[i] + v[j] + v[z] <= M && v[i] + v[j] + v[z] > gap) {
					gap = v[i] + v[j] + v[z];
				}
			}
		}
	}

	cout << gap;
	return 0;
}