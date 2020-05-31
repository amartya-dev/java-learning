package whileAndDowhileLoops;

import java.util.Scanner;

public class SumOfDigits {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		
		int x=n;
		int s=0;
		while (x>0)
		{
			s+=x%10;
			x=x/10;
		}
		System.out.println(s);
	}

}
