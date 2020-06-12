package arrays;

public class Sort012 {
	
	
	public static void sort012(int a[], int n){
	    // code here 
	    
	    int arr[] = new int[3];
	    
	    for (int i=0;i<a.length;i++)
	    {
	        if (a[i]==0)
	        {
	            arr[0]+=1;
	        }
	        else if (a[i]==1)
	        {
	            arr[1]+=1;
	        }
	        else if (a[i]==2)
	        {
	            arr[2]+=1;
	        }
	    }
	    
	    for (int j=0;j<3;j++)
	    {
	        for(int k=0;k<arr[j];k++)
	        {
	            System.out.print(j);
	        }
	        
	        
	    }
	    System.out.println();
	    
	    
	    
	    
	}


	public static void main(String[] args) {
		
	    int arr[] = { 0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1 }; 
	    int n = arr.length; 
	    sort012(arr, n); 
	
	}

}
