import java.util.*;

class Solution {
    public int[] solution(int l, int r) {
        List<Integer> result = new ArrayList<>();
        for (int i = l; i <= r; i++) {
            String num = String.valueOf(i);
            boolean notZeroOrFive = false;
            for (char n: num.toCharArray()) {
                if (n != '5' && n != '0') notZeroOrFive = true;
            }
            if (notZeroOrFive) {
                continue;
            }
            result.add(i);
        }
        
        if (result.size() == 0) {
            return new int[]{-1};
        }
        
        int[] array = new int[result.size()];
        for (int i = 0; i < result.size(); i++) {
            array[i] = result.get(i);
        }
        return array;
    }
}