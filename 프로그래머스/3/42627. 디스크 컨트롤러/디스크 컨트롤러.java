import java.util.*;

class Solution {
    public int solution(int[][] jobs) {
       int answer = 0;
        int time = 0;
        int idx = 0;
        int completedJobs = 0;
        
        Arrays.sort(jobs, Comparator.comparingInt(a -> a[0]));
        
        Queue<int[]> q = new PriorityQueue<>(Comparator.comparingInt(a -> a[1]));

        while (completedJobs < jobs.length) {
            while (idx < jobs.length && jobs[idx][0] <= time) {
                q.offer(jobs[idx]);
                idx++;
            }

            if (!q.isEmpty()) {
                int[] currentJob = q.poll();
                time += currentJob[1];
                answer += (time - currentJob[0]);
                completedJobs++;
            } else {
                time = jobs[idx][0];
            }
        }

        return answer / jobs.length;
    }
}