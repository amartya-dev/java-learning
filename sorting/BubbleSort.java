package sorting;

import java.util.Scanner;

public class BubbleSort {

	public static void main(String[] args) {
		
		
		//Scanner sc = new Scanner(System.in);
		 int [] A = {4,6,2,7,3,9,1,10,-1,-2,-10,-11,12,3,54,33,-11111};
		 int n=A.length;
		 
		 for(int i=0;i<n-1;i++)
		 {
			 boolean sorted=true;
			 for (int j=0; j<n-1-i;j++)
			 {
				 if (A[j+1]<A[j])
				 {
					 int temp = A[j];
					 A[j]=A[j+1];
					 A[j+1]=temp;
					 sorted=false;
				 }
			 }
			 
			 if (sorted)
			 {
				 break;
			 }
		 }
		 
		 for (int i=0;i<n;i++)
		 {
			 System.out.print(A[i]+" ");
		 }
		 
		
	}

}
