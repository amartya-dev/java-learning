package patternPractice;

import java.util.Scanner;

public class RightTriangleWithEmptyInMiddle {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();

		System.out.println("*");
		
		for (int i= 2 ; i< n; i++) {
			
			System.out.print("* ");
			for (int j=2;j<i;j++)
			{
				System.out.print("  ");
			}
			System.out.print("*\n");
		}
		for (int i=0;i<n;i++) {
			System.out.print("* ");
		}
		
	}

}
