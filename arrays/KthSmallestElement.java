package arrays;
// https://practice.geeksforgeeks.org/problems/kth-smallest-element/0
public class KthSmallestElement {

	public static void main(String[] args) {
		
		
		int n=7;
		int a[]= {99,1,2,9,33,0,4,5,6,7};
		int k=4;
		
		int sm[]= new int[n];
		sm[0]=a[0];
		int ind=0;
		for (int i=0;i<n;i++)
		{
			if (a[i]>sm[ind])
			{
				sm[ind+1]=a[i];
				ind+=1;
			}
		}
		for(int i=0;i<n;i++)
		{
			System.out.println(sm[i]);
		}

	}

}
