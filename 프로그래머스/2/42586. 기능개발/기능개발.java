import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        Queue<Integer> q = new LinkedList<>();
        List<Integer> result = new ArrayList<>();
        
        for (int i = 0; i< progresses.length; i++) {
            double remain = (100 - progresses[i]) / (double) speeds[i];
            int days = (int) Math.ceil(remain);
            
            if (!q.isEmpty() && q.peek() < days) {
                result.add(q.size());
                q.clear();
            }
            
            q.offer(days);
        }
        
        result.add(q.size());
        
        return result.stream().mapToInt(i -> i).toArray();
    }
}