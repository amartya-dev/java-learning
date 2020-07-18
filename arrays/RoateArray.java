package arrays;

public class RoateArray {

	public static void main(String[] args) {
		
		int n=7;
		int d=2;
		
		int a[]= {2,3,4,5,6,52,44,12};
		
		for (int i=d;i<n;i++)
		{
			System.out.print(a[i]);
			System.out.print(" ");
		}
		
		for(int i=0;i<d;i++)
		{
			System.out.print(a[i] );
			System.out.print(" ");
		}

	}

}
