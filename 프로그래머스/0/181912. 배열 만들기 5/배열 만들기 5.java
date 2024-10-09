import java.util.*;

class Solution {
    public int[] solution(String[] intStrs, int k, int s, int l) {
        List<Integer> result = new ArrayList<>();
        
        for (String intStr: intStrs) {
            Integer num = Integer.parseInt(intStr.substring(s, s + l));
            if (num > k) {
                result.add(num);
            }
        }
        
        return result.stream().mapToInt(i -> i).toArray();
    }
}