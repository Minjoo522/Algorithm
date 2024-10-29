import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        Queue<Process> q = new LinkedList<>();
        for (int i = 0; i < priorities.length; i++) {
            q.offer(new Process(priorities[i], i));
        }
        
        int order = 0;
        
        while (!q.isEmpty()) {
            Process current = q.poll(); // 앞 요소 제거
            boolean hasHigherProcess = false;
            
            for (Process p: q) {
                if (p.priority > current.priority) {
                    hasHigherProcess = true;
                    break;
                }
            }
            
            if (hasHigherProcess) {
                q.offer(current);
            } else {
                order++;
                if (current.location == location) {
                    return order;
                }
            }
        }
        return -1;
    }
    
    private class Process {
        
        int priority;
        int location;
        
        Process(int priority, int location) {
            this.priority = priority;
            this.location = location;
        }
    }
}