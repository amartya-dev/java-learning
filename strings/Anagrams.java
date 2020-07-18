package strings;

import java.util.Scanner;

public class Anagrams {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		System.out.println("enter String 1");
		String a =sc.nextLine();
		
		System.out.println("enter String 2");
		String b = sc.nextLine();
		
		
		int[] al= new int[256];
		
		boolean isAnagram = true;
		
		if(a.length()==b.length())
		{
			for (int i=0;i<a.length();i++)
			{
				int index=(int) a.charAt(i);
				al[index]+=1;
				
			}
			for (int i=0;i<a.length();i++)
			{
				int index=(int) b.charAt(i);
				al[index]-=1;
				
			}
			
			for (int i=0;i<256;i++)
			{
				if(al[i]!=0)
				{
					isAnagram=false;
					break;
				}
				
			}
			
			if (isAnagram)
			{
				System.out.println("Yes");
			}
			else
			{
				System.out.println("No");
			}
		}
		else
		{
			System.out.println("No");
		}

	}

}
