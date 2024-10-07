import java.lang.*;

class Solution {
    public String solution(String my_string, int[][] queries) {
        String current = my_string;
        for (int[] query: queries) {
            StringBuffer sb = new StringBuffer();
            int s = query[0];
            int e = query[1];
            
            for (int i = 0; i < s; i++) {
                System.out.println("i 1 = " + i);
                sb.append(current.charAt(i));
            }
            
            for (int i = e; i >= s; i--) {
                System.out.println("i = " + i);
                sb.append(current.charAt(i));
            }
            
            for (int i = s + 1; i < current.length(); i++) {
                sb.append(current.charAt(i));
            }
            current = sb.toString();
        }
        return current;
    }
}