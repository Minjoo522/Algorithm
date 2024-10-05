import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        StringBuilder sb = new StringBuilder();
        
        for (int i = 0; i < a.length(); i++) {
            char currentChar = a.charAt(i);
            
            if (Character.isLowerCase(currentChar)) {
                sb.append(Character.toUpperCase(currentChar));
            } else {
                sb.append(Character.toLowerCase(currentChar));
            }
        }
        System.out.println(sb.toString());
    }
}