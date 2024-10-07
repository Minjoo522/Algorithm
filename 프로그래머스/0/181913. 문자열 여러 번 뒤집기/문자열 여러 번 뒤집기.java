import java.lang.*;

class Solution {
    public String solution(String my_string, int[][] queries) {
        String current = my_string;
        for (int[] query: queries) {
            int s = query[0];
            int e = query[1];
            
            String prefix = current.substring(0, s);
            String toReverse = new StringBuilder(current.substring(s, e + 1)).reverse().toString();
            String suffix = current.substring(e + 1);
            
            current = prefix + toReverse + suffix;
        }
        return current;
    }
}