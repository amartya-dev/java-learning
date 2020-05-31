package arrays;

import java.util.Scanner;

public class MatrixMultiplication {

	public static void main(String[] args) {
		
		
		Scanner sc = new Scanner(System.in);
		
		System.out.println("enter Matrix A dimensions");
		int m =sc.nextInt();
		int n = sc.nextInt();
		
		System.out.println("enter Matrix b dimensions");
		int p =sc.nextInt();
		int q = sc.nextInt();
		
		if (n!=p)
		{
			System.out.println("Invalid Matrix operation");
		}
		else
		{
			int [][] a = new int[m][n];
			int [][] b = new int[p][q];
			
			System.out.println("Enter A matrix vals");
			
			for (int row =0;row<m;row++)
			{
				for (int col=0;col<n;col++)
				{
					System.out.println("enter A["+ row+"]["+col+"]");
					a[row][col]=sc.nextInt();
				}
			}
			
			
			System.out.println("Enter B matrix vals");
			
			for (int row =0;row<p;row++)
			{
				for (int col=0;col<q;col++)
				{
					System.out.println("enter B["+ row+"]["+col+"]");
					b[row][col]=sc.nextInt();
				}
			}
			
			int[][] c= new int[m][q];
			
			for (int row =0;row<m;row++)
			{
				for (int col=0;col<q;col++)
				{
					for (int x=0;x<n;x++)
					{
						c[row][col]+=a[row][x]*b[x][col];
					}
					
					System.out.print(c[row][col]);
					
				}
				System.out.println();
			}
			
			
		}
		
		
		

		

	}

}
