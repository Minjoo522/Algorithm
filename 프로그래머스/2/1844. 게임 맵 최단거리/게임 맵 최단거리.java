import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        int rows = maps.length;
        int cols = maps[0].length;
        
        Queue<int[]> q = new LinkedList<>();
        boolean[][] visited = new boolean[rows][cols];
        int[][] directions = {{0, -1}, {0, 1}, {1, 0}, {-1, 0}};
        
        q.add(new int[]{0, 0, 1});
        visited[0][0] = true;
        
        while(!q.isEmpty()) {
            int[] current = q.poll();
            int x = current[0];
            int y = current[1];
            int distance = current[2];
            
            if (x == rows - 1 && y == cols - 1) {
                return distance;
            }
            
            for (int[] direction: directions) {
                int nx = x + direction[0];
                int ny = y + direction[1];
                
                if (nx >= 0 && nx < rows && ny >= 0 && ny < cols && maps[nx][ny] == 1 && !visited[nx][ny]) {
                    visited[nx][ny] = true;
                    q.offer(new int[]{nx, ny, distance + 1});
                }
            }
        }
        
        return -1;
    }
}