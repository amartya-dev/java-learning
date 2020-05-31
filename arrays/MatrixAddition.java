package arrays;

import java.util.Scanner;

public class MatrixAddition {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int m =sc.nextInt();
		int n = sc.nextInt();
		int [][] a = new int[m][n];
		int [][] b = new int[m][n];
		
		System.out.println("Enter A matrix vals");
		
		for (int row =0;row<m;row++)
		{
			for (int col=0;col<n;col++)
			{
				System.out.println("enter A matrix val");
				a[row][col]=sc.nextInt();
			}
		}
		
		System.out.println("Enter B matrix vals");
		
		for (int row =0;row<m;row++)
		{
			for (int col=0;col<n;col++)
			{
				System.out.println("enter B matrix val");
				b[row][col]=sc.nextInt();
			}
		}
		
		int [][] c = new int[m][n];
		
		System.out.println("Answer is ");
		
		for (int row =0;row<m;row++)
		{
			for (int col=0;col<n;col++)
			{
				c[row][col]=a[row][col]+b[row][col];
				System.out.print(c[row][col]);
				
			}
			System.out.println();
		}
		

	}

}
