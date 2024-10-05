import java.util.*;
import java.lang.Math;

class Solution {
    public int solution(int a, int b, int c) {
        Set<Integer> nums = new HashSet(Arrays.asList(a, b, c));
        int answer = a + b + c;
        
        if (nums.size() == 3) {
            return answer;
        }
        if (nums.size() <= 2) {
            answer *= Math.pow(a, 2) + Math.pow(b, 2) + Math.pow(c, 2);
        }
        if (nums.size() <= 1) {
            answer *= Math.pow(a, 3) + Math.pow(b, 3) + Math.pow(c, 3);
        }
        return answer;
    }
}