import java.util.*;

class Solution {
    private static final int[] dx = {0, 0, -1, 1};
    private static final int[] dy = {-1, 1, 0, 0};
    private static final Queue<int[]> q = new LinkedList<>();
    private static boolean[][] visited;
    
    public int solution(int[][] maps) {
        return bfs(maps, 0, 0);
    }
    
    private int bfs(int[][] maps, int startX, int startY) {
        int rows = maps.length;
        int cols = maps[0].length;
        
        visited = new boolean[maps.length][maps[0].length];
        
        q.add(new int[]{startX, startY, 1});
        visited[startX][startY] = true;
        
        while (!q.isEmpty()) {
            int[] current = q.poll();
            int x = current[0];
            int y = current[1];
            int distance = current[2];
            
            if (x == rows - 1 && y == cols - 1) {
                return distance;
            }
            
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                
                if (nx >= 0 && nx < rows && ny >= 0 && ny < cols && maps[nx][ny] != 0 && !visited[nx][ny]) {
                    visited[nx][ny] = true;
                    q.add(new int[]{nx, ny, distance + 1});
                }
            }
        }
        
        return -1;
    }
}