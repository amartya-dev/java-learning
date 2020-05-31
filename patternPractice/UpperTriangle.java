package patternPractice;

import java.util.Scanner;

public class UpperTriangle {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		
		for (int i=1;i<n+1;i++)
		{
			for (int j=n+1;j>i;j--) {
				System.out.print("* ");
			}
			System.out.println();
		}

	}

}
