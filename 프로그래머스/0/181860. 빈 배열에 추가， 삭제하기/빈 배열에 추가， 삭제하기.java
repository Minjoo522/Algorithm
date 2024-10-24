import java.util.*;

class Solution {
    public int[] solution(int[] arr, boolean[] flag) {
        List<Integer> result = new ArrayList<>();
        
        for (int i = 0; i < arr.length; i++) {
            if (flag[i]) {
                for (int j = 1; j <= arr[i] * 2; j++) {
                    result.add(arr[i]);
                }
            } else {
                for (int k = 0; k < arr[i]; k++) {
                    result.remove(result.size() - 1);
                }
            }
        }
        return result.stream().mapToInt(i -> i).toArray();
    }
}