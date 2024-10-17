import java.util.*;

class Solution {
    public int[] solution(String my_string) {
        int[] ascii = new int[52];
        
        for (char c: my_string.toCharArray()) {
            if (c >= 'A' && c <= 'Z') {
                ascii[c - 'A']++;
            } else if (c >= 'a' && c <= 'z') {
                ascii[c - 'a' + 26]++;
            }
        }
        return ascii;
    }
}