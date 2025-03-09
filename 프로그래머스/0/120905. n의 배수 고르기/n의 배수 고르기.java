import java.util.*;

class Solution {
    public int[] solution(int n, int[] numlist) {
        List<Integer> result = new ArrayList<>();
        
        for (int i = 0; i < numlist.length; i++) {
            if (numlist[i] % n == 0) {
                result.add(numlist[i]);
            }
        }
        
        return result.stream().mapToInt(Integer::intValue).toArray();
    }
}