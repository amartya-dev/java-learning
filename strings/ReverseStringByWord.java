package strings;

import java.util.Scanner;

public class ReverseStringByWord {

	public static void main(String[] args) {
		
		
		Scanner sc = new Scanner(System.in);
		
		System.out.println("enter String ");
		String a =sc.nextLine();
		
		String[] arr=a.split(" +");
		
		String[] arr2= new String[arr.length];
		//System.out.println("ok");
		for(int i=arr.length-1;i>=0;i--)
		{
			arr2[arr.length-1-i]=arr[i];
		}
		
		for(String w : arr2)
		{
			System.out.print(w+' ');
		}
		
		System.out.println("*");

	}

}
