import java.util.*;

public class bubbleSort {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int numInput = scanner.nextInt();
        int arr[] = new int[numInput];
        for (int i = 0; i < numInput; i ++){
            arr[i] = scanner.nextInt();
        }
        for(int i = 0; i < numInput; i ++){
            for (int j = 0; j < numInput-i-1; j++){
                if (arr[j] > arr[j+1]){
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
            }
        }
        for (int i = 0; i < numInput; i ++){
            System.out.printf("%d ", arr[i]);
        }
        scanner.close();
    }
}
