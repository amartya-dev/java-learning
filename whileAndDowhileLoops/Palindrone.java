package whileAndDowhileLoops;

import java.util.Scanner;

public class Palindrone {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();

		int x=n;
		int s=0;
		int r=0;
		while(x>0)
		{
			r=x%10;
			s=s*10+r;
			x=x/10;
		}
		if (s==n) {
			System.out.println("Palindrome");
		}
		else
		{
			System.out.println("Not Palindrome");
		}
		//System.out.println(s);
	}

}
