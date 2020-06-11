import java.util.*;

public class mergeSort {
    void merge(int arr[], int start, int mid, int stop) {
        // This function will first get the respective halves and
        // then merge according to the ascending order

        // Get the number of elements in both the halves
        int numLeft = mid - start + 1;
        int numRight = stop - mid;

        // Create empty left and right arrays
        int leftSubArray[] = new int[numLeft];
        int rightSubArray[] = new int[numRight];

        // Populate both the arrays
        for (int leftIter = 0; leftIter < numLeft; leftIter++) {
            leftSubArray[leftIter] = arr[start + leftIter];
        }
        for (int rightIter = 0; rightIter < numRight; rightIter++) {
            rightSubArray[rightIter] = arr[mid + rightIter + 1];
        }

        // Compare and change values in the main array
        int leftIter = 0, rightIter = 0;
        int arrayIter = start;

        // First deal with the common number or elements
        while (leftIter < numLeft && rightIter < numRight) {
            if (leftSubArray[leftIter] < rightSubArray[rightIter]) {
                arr[arrayIter] = leftSubArray[leftIter];
                leftIter++;
            } else {
                arr[arrayIter] = rightSubArray[rightIter];
                rightIter++;
            }
            arrayIter++;
        }

        // Copy the remaining elements from the left sub array
        while (leftIter < numLeft) {
            arr[arrayIter] = leftSubArray[leftIter];
            leftIter++;
            arrayIter++;
        }

        // Copy the remaining elements from the right sub array
        while (rightIter < numRight) {
            arr[arrayIter] = rightSubArray[rightIter];
            rightIter++;
            arrayIter++;
        }
    }

    // The main function to recursively sort the array
    void sort(int arr[], int start, int stop) {
        // Recursion Stopping condition
        if (start < stop) {
            int mid = (start + stop) / 2;

            // Sort the left array
            sort(arr, start, mid);
            // Sort the right array
            sort(arr, mid + 1, stop);

            // Merge the arrays
            merge(arr, start, mid, stop);
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int numInput = scanner.nextInt();
        int arr[] = new int[numInput];
        for (int i = 0; i < numInput; i++) {
            arr[i] = scanner.nextInt();
        }

        mergeSort mergeSortObject = new mergeSort();
        mergeSortObject.sort(arr, 0, arr.length - 1);

        for (int i = 0; i < arr.length; i++) {
            System.out.printf("%d ", arr[i]);
        }
        scanner.close();
    }
}
