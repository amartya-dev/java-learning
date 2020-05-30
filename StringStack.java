import java.util.*;

public class StringStack {
    public static void main(String[] args) {
        Stack<String> stack = new Stack<String>();
        stack.push("/");
        String sub = stack.pop();
        String result = (sub == "/") ? "yes" : "No";
        System.out.println(sub + result);
    }
}
