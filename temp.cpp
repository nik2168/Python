#include <iostream>
#include <vector>
using namespace std;

int main()
{

    vector<int> v = {1, 2, 3, 4};

    int count = 0;
    int k = 5;

    for (int i = 0; i < v.size(); i++)
    {
        for (int j = i; j < v.size(); j++)
        {
            int sum = 0;
            for (int k = i; k < j; k++)
            {
                sum += v[k];

                cout << v[k] << " ";
            }
            cout << endl;
            if (sum == k)
                count++;
        }
    }

    cout << "ans : " << count;

    return 0;
}