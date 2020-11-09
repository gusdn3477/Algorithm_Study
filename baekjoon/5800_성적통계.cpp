#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int main(void) {

	cin.tie(0);
	cin.sync_with_stdio(false);
	vector<int> v;
	int N, M, temp;
	int max_;

	cin >> N;

	for (int i = 1; i <= N; i++) {
		cin >> M;
		max_ = 0;
		for (int j = 0; j < M; j++) {
			cin >> temp;
			v.push_back(temp);
		}

		sort(v.begin(), v.end(), greater<int>());
		max_ = v[0] - v[1];

		for (int j = 1; j < M-1; j++) {
			max_ = max(max_, v[j] - v[j + 1]);
		}

		cout << "Class " << i << "\n";
		cout << "Max " << v[0] << ", Min " << v[v.size() - 1] << ", Largest gap " << max_ << "\n";

		v.clear();
	}

	return 0;
}