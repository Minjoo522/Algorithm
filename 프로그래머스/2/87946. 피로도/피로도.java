import java.util.*;

class Solution {
    public int solution(int k, int[][] dungeons) {
        return dfs(k, dungeons, new boolean[dungeons.length], 0);
    }
    
    private int dfs(int current, int[][] dungeons, boolean[] visited, int count) {
        int maxDungeons = count;
        
        for (int i = 0; i < dungeons.length; i++) {
            if (!visited[i] && current >= dungeons[i][0]) {
                visited[i] = true;
                maxDungeons = Math.max(maxDungeons, dfs(current - dungeons[i][1], dungeons, visited, count + 1));
                visited[i] = false;
            }
        }
        
        return maxDungeons;
    }
}