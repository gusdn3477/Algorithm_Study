#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <cstdio>
#include <queue>

using namespace std;

int main(void) {

	queue<int> q;
	int a,N;

	cin.tie(NULL);
	cin.sync_with_stdio(false);
	
	cin >> N;
	for (int i = 1; i <= N; i++)
		q.push(i);

	while (q.size() != 1) {
		q.pop();
		a = q.front();
		q.pop();
		q.push(a);
	}

	cout << q.front();
  
	return 0;
}
