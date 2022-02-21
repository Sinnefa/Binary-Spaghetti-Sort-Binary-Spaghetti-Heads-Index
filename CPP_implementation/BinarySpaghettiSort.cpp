#include <algorithm>
#include <cmath>
#include <iostream>
#include <chrono>

using namespace std;

void BinarySpaghettiSort(int *values, int *sorted, int length)
{
    if (length>30) { // C++ doesn't allow arbirarely big integer thus arrays can't be longer then this
                     // Use an external libary like gmp or ttmath
        return;
    }

    int maximum = *std::max_element(values,values+length);
    int minimum = *std::min_element(values,values+length);
    unsigned long long int spaghetti_heads[maximum-minimum+1] = {};
    unsigned long long int xor_value = 0;
    int index = 0;
    int n = 0;
    unsigned long long int k = 0;

    for (int i = 0 ; i < length ; i += 1)
      spaghetti_heads[values[i]-minimum] += 1 << (length-i-1);

	int shlength = sizeof(spaghetti_heads)/sizeof(spaghetti_heads[0]);

    for (int i = 0 ; i < shlength ; i += 1)
    {
      xor_value = spaghetti_heads[i];
      while (xor_value > 0) {
        k = (unsigned long long int) log2(xor_value);
        sorted[index] = values[length-k-1];
        xor_value = xor_value ^ (1 << k);
        index += 1;
      }
    }
}

int main()
{
    int length = 30; // C++ doesn't allow arbirarely long integer thus arrays can't be longer then this
    int arr[length];
    for(int i=0;i<length;i++)
        arr[i]=1+(rand()%100);
	int result[length] = {};

	cout << "Starting array " << endl;
    for (int i = 0; i < length; i++)
        cout << arr[i] << " ";

    auto start = std::chrono::high_resolution_clock::now();

	BinarySpaghettiSort(arr, result, length);

	auto finish = std::chrono::high_resolution_clock::now();
	auto microseconds = std::chrono::duration_cast<std::chrono::microseconds>(finish-start);

	cout << endl << "Binary Spaghetti Sorted array " << endl;
    for (int i = 0; i < length; i++)
        cout << result[i] << " ";
    cout << endl << "Binary Spaghetti sort took: " << microseconds.count() << "µs\n";


    start = std::chrono::high_resolution_clock::now();

    sort(arr, arr + length);

	finish = std::chrono::high_resolution_clock::now();
	microseconds = std::chrono::duration_cast<std::chrono::microseconds>(finish-start);

    cout << "\nArray after default sort: " << endl;
    for (int i = 0; i < length; ++i)
        cout << arr[i] << " ";
    cout << endl << "Default sort took: " << microseconds.count() << "µs\n";

    return 0;
}


