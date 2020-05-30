import java.io.*;
import java.util.*;

public class Solution {

    public static int [] computeSignature()

    public static ArrayList <String> getAllSubstrings (String str){
        ArrayList<String> allSubString = new ArrayList<String>();
        for (int firstElem = 0; firstElem < str.length(); firstElem ++){
            for (int lastElem = firstElem; lastElem <= str.length(); lastElem ++){
                String toAppend = str.substring(firstElem, lastElem);
                if (toAppend.equals("") || toAppend.equals(" ")){
                    continue;
                }
                allSubString.add(toAppend);
            }
        }
        return allSubString;
    }

    // Complete the sherlockAndAnagrams function below.
    static int sherlockAndAnagrams(String s) {
        int countAnagrams = 0;
        ArrayList <String> allSubStrings = getAllSubstrings(s);
        System.out.println(allSubStrings);
        for (int iter = 0; iter < allSubStrings.size(); iter++){
            for (int iter2 = iter + 1; iter2 < allSubStrings.size(); iter2++){
                if (isAnagram(allSubStrings.get(iter), allSubStrings.get(iter2))){
                    countAnagrams ++;
                }
            }
        }
        return (countAnagrams);
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int q = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int qItr = 0; qItr < q; qItr++) {
            String s = scanner.nextLine();

            int result = sherlockAndAnagrams(s);

            bufferedWriter.write(String.valueOf(result));
            bufferedWriter.newLine();
        }

        bufferedWriter.close();

        scanner.close();
    }
}
