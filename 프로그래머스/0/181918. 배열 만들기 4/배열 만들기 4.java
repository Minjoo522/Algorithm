import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        Deque<Integer> stk = new ArrayDeque<>();
        int i = 0;
        
        while (i < arr.length) {
            if (stk.isEmpty()) {
                stk.push(arr[i]);
                i++;
            } else {
                if (stk.peek() < arr[i]) {
                    stk.push(arr[i]);
                    i++;
                } else {
                    stk.pop();
                }
            }
        }
        int[] result = stk.stream().mapToInt(j -> j).toArray();
        Arrays.sort(result);
        return result;
    }
}