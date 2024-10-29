import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        Queue<Integer> heap = new PriorityQueue<>();
        
        for (int i = 0; i < scoville.length; i++) {
            heap.offer(scoville[i]);
        }
        
        int answer = 0;
        
        while (heap.size() > 1) {
            if (heap.peek() >= K) {
                return answer;
            }
            
            int notSpicy1 = heap.poll();
            int notSpicy2 = heap.poll();
            int mixed = notSpicy1 + (notSpicy2 * 2);
            
            heap.offer(mixed);
            answer++;
        }
        
        return heap.peek() >= K ? answer : -1;
    }
}