import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        List<Integer> nums = new ArrayList<>();
        
        int prev = -1;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] != prev) {
                nums.add(arr[i]);
                prev = arr[i];
            }
        }

        return nums.stream().mapToInt(i -> i).toArray();
    }
}