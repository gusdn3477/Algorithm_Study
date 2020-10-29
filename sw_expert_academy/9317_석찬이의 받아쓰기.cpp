#include<iostream>
#include <string>

using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T, A, B;
	int count = 0;
	string a, b;
	cin >> T;
	/*
	   여러 개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
	*/
	for (test_case = 1; test_case <= T; ++test_case)
	{
		cin >> A;
		count = 0;
		cin >> a;
		cin >> b;
		for (int i = 0; i < A; i++) {
			if (a[i] == b[i])
				count++;
		}
		cout << "#" << test_case << " " << count << endl;
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}