#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <assert.h>
void insertionSort(int ar_size, int *  ar) {
	int i,j,temp,n=ar_size,p;
	temp=ar[n-1];
    
		for(j=n-2;j>=0;j--)
		{
			if(ar[j]>temp)
			{
				ar[j+1]=ar[j];
			}
			else
				break;
		
			
			
			for(p=0;p<n;p++)
				printf("%d ",ar[p]);
			printf("\n");
        }
    ar[j+1]=temp;
			for(p=0;p<n;p++)
				printf("%d ",ar[p]);
			printf("\n");
}
int main(void) {
   
   int _ar_size;
scanf("%d", &_ar_size);
int _ar[_ar_size], _ar_i;
for(_ar_i = 0; _ar_i < _ar_size; _ar_i++) { 
   scanf("%d", &_ar[_ar_i]); 
}

insertionSort(_ar_size, _ar);
   
   return 0;
}
