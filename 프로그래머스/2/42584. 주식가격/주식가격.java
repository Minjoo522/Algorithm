import java.util.*;

class Solution {
    public int[] solution(int[] prices) {
        int n = prices.length;
        int[] answer = new int[n];
        Deque<Integer> stack = new ArrayDeque<>();
        
        for (int i = 0; i < n; i++) {
            
            while (!stack.isEmpty() && prices[stack.peekLast()] > prices[i]) {
                int j = stack.removeLast();
                answer[j] = i - j;
            }
            
            stack.addLast(i);
        }
        
        while (!stack.isEmpty()) {
            int j = stack.removeLast();
            answer[j] = n - j - 1;
        }
        
        return answer;
    }
}