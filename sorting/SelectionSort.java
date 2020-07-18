package sorting;

public class SelectionSort {

	public static void main(String[] args) {
		
		int [] A = {4,6,2,7,3,9,1,10,-1,-2,-10,-11,12,3,54,33,-111};
		int n=A.length;
		
		for (int i=0;i<n-1;i++)
		{
			int minIndex=i;
			for (int j=i;j<n;j++)
			{
				if (A[j]<A[minIndex])
				{
					minIndex=j;
				}
			}
			int temp=A[i];
			A[i]=A[minIndex];
			A[minIndex]=temp;
		}
		
//		for (int i=0;i<n;i++)
//		{
//			System.out.print(A[i]+" ");
//		}

		for (int e: A)
		{
			System.out.print(e+" ");
		}
	}

}
