package arrays;

//https://practice.geeksforgeeks.org/problems/sum-of-lengths-of-non-overlapping-subarrays/0

public class SumofLengthsOfSubArrays {

	
	public static int maxlen(int arr[],int n, int k)
	{
		int lengths[]=new int[n];
		int check[]=new int[n];
		int c=0;
		for (int i=0;i<n;i++)
		{
			if (arr[i]<=k)
			{
				lengths[c]+=1;
				
			}
			if (arr[i]==k)
			{
				check[c]=1;
			}
			if (arr[i]>k)
			{
				if (check[c]==0)
				{
					lengths[c]=0;
				}
				c+=1;
			}
		}
		int s=0;
		for (int i=0;i<n;i++)
		{
			s+=lengths[i];
			System.out.print(lengths[i]);
			System.out.print(' ');
		}
		System.out.println();
		return s;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int arr[]= {4, 5, 7, 1, 2, 9, 8, 4, 3, 1};
		int n=10;
		int k=4;
		System.out.println(maxlen(arr,n,k));
	}

}
