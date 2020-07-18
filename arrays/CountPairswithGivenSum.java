package arrays;
//https://practice.geeksforgeeks.org/problems/count-pairs-with-given-sum/0
// Can do better
public class CountPairswithGivenSum {
	
	public static int countPairs(int arr[],int n, int k)
	{
		int c=0;
		for (int i=0;i<n;i++)
		{
			for (int j=i+1;j<n;j++)
			{
				if(arr[i]+arr[j]==k)
				{
					c+=1;
				}
			}
		}
		return c;
	}

	public static void main(String[] args) {
		int arr[]= {1,1,1,1};
		int n=4;
		int k=2;
		System.out.println(countPairs(arr,n,k));

	}

}
