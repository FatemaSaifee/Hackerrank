#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <map>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    
    string str;int len,i=0,j=0,k=0;char temp;
    int t,q;
    cin>>t;
    for(q=0;q<t;q++)
    {
        i=j=k=0;
    cin>>str;
    len = str.length();
    map<string,int>m;
    while(i<len)
    {
        temp = str[0];
        while(j<len-1)
        {
            str[j] = str[j+1];
            j++;
        }
        str[j] = temp;
        m[str] = k;
        k++;
        i++;j=0;
    }
    str = m.rbegin()->first;
    cout<<str<<"\n";
    }
    
    return 0;
}
