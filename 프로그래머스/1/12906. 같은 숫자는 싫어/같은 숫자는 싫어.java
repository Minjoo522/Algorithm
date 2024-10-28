import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        Stack<Integer> nums = new Stack<>();
        
        nums.push(arr[0]);
        for (int i = 1; i < arr.length; i++) {
            if (nums.peek() != arr[i]) {
                nums.push(arr[i]);
            }
        }
        
        int[] result = new int[nums.size()];
        for (int i = nums.size() - 1; i >= 0; i--) {
            result[i] = nums.pop();
        }
        return result;
    }
}