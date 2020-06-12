package arrays;
//https://practice.geeksforgeeks.org/problems/find-transition-point-1587115620/1
public class TransitionPoint {

	public static void main(String[] args) {
	    int transitionPoint(int arr[], int n) {
	        // code here
	        int c=0;
	        boolean onePresent=false;
	        for (int i=0;i<n;i++)
	        {
	            if (arr[i]==1)
	            {
	                onePresent=true;
	                c=i;
	                break;
	            }
	        }
	        if (!onePresent)
	        {
	            c=-1;
	        }
	        return c;
	    }
	}

	}

}
