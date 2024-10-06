import java.util.*;

class Solution {
    public int[] solution(int n) {
        List<Integer> result = new ArrayList<>();
        int x = n;
        
        while (x != 1) {
            result.add(x);
            if (x % 2 == 0) {
                x /= 2;
            } else {
                x = 3 * x + 1;
            }
        }
        result.add(1);
        return result.stream().mapToInt(i -> i).toArray();
    }
}