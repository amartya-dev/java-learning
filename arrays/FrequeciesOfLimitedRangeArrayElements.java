class Frequency{
    public static void frequencycount(int arr[], int n)
    {
        // code here
        int arrf[]= new int[n];
        for (int a: arr)
        {
            arrf[a-1]++;
        }
        for (int i=0;i<arrf.length;i++)
        {
            arr[i]=arrf[i];
        }
  
    }
}