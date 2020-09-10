// Даны два числа A и B. Вам нужно вычислить их сумму A+B. В этой задаче вам нужно читать из стандартного ввода и выводить ответ в стандартный вывод
#include <iostream>
#include <fstream>
using namespace std;

int main() {
    int data1, data2, sum;
    ifstream myfile;
    myfile.open("input.txt");
    myfile >> data1;
    myfile >> data2;
    sum = data1 + data2;
    ofstream Newfile("output.txt");
    Newfile << sum << endl;
    myfile.close();
    return 0;
}