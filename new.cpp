#include<iostream>

using namespace std;

int main(){
	int num1, num2, temp;
	temp = 0;
	cout << "Enter the num1 and num2:" << endl;
	cin >> num1 >> num2;
	num1 = temp;
	num2 = num1;
	temp = num2;
	cout << "Num1: " << num1 << "Num2: " << num2;

}