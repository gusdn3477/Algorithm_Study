#include <iostream>
#include <stack>
#include <queue>
#include <cstring>

using namespace std;

int N, M, V;
int arr[1001][1001];
int visited[1001];
queue<int> q;
void DFS(int x);
void BFS(int x);

int main(void) {

	cin.sync_with_stdio(false);
	cin.tie(0);
	int x, y;

	cin >> N >> M >> V;

	for (int i = 0; i < M; i++) {
		cin >> x >> y;
		arr[x][y] = 1;
		arr[y][x] = 1;
	}

	DFS(V);
	memset(visited, 0, sizeof(visited));
	cout << "\n";

	BFS(V);

	return 0;
}

void DFS(int x) {

	cout << x << " ";
	visited[x] = 1;
	for (int i = 1; i <= N; i++) {
		if (visited[i] == 0 && arr[x][i] == 1) {
			DFS(i);
		}
	}
}

void BFS(int x) {

	visited[x] = 1;
	int save;
	q.push(x);

	while (!q.empty()) {
		save = q.front();
		q.pop();
		cout << save << " ";
		for (int i = 1; i <= N; i++) {
			if (visited[i] == 0 && arr[save][i] == 1) {
				q.push(i);
				visited[i] = 1;
			}
		}
	}
}