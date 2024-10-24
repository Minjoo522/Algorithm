import java.util.*;

class Solution {
    public int[] solution(int[] arr, int k) {
        List<Integer> nums = new ArrayList<>();
        
        for (int num: arr) {
            if (!nums.contains(num)) {
                nums.add(num);
            }
        }
        
        int[] result = new int[k];
        Arrays.fill(result, -1);
        
        for (int i = 0; i < Math.min(k, nums.size()); i++) {
            result[i] = nums.get(i);
        }
        
        return result;
    }
}