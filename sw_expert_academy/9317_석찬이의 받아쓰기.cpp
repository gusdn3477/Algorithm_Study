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
	   ���� ���� �׽�Ʈ ���̽��� �־����Ƿ�, ������ ó���մϴ�.
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
	return 0;//��������� �ݵ�� 0�� �����ؾ��մϴ�.
}