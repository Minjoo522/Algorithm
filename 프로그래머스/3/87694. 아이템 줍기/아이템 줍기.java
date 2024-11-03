import java.util.*;

class Solution {
    private static final int SIZE = 101;
    private static final int[][] directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    
    public int solution(int[][] rectangle, int characterX, int characterY, int itemX, int itemY) {
        boolean[][] map = new boolean[SIZE * 2][SIZE * 2];
        
        for (int[] rec : rectangle) {
            int x1 = rec[0] * 2, y1 = rec[1] * 2;
            int x2 = rec[2] * 2, y2 = rec[3] * 2;
            
            for (int i = x1; i <= x2; i++) { // 가로
                map[i][y1] = true;
                map[i][y2] = true;
            }
            
            for (int i = y1; i <= y2; i++) { // 세로
                map[x1][i] = true;
                map[x2][i] = true;
            }
        }
        
        for (int[] rec : rectangle) {
            int x1 = rec[0] * 2 + 1, y1 = rec[1] * 2 + 1;
            int x2 = rec[2] * 2 - 1, y2 = rec[3] * 2 - 1;
            
            for (int i = x1; i <= x2; i++) {
                for (int j = y1; j <= y2; j++) {
                    map[i][j] = false;
                }
            }
        }
        
        Queue<int[]> q = new LinkedList<>();
        boolean[][] visited = new boolean[SIZE * 2][SIZE * 2];
        
        int startX = characterX * 2;
        int startY = characterY * 2;
        int targetX = itemX * 2;
        int targetY = itemY * 2;
        
        q.add(new int[]{startX, startY, 0});
        visited[startX][startY] = true;
        
        while(!q.isEmpty()) {
            int[] current = q.poll();
            int x = current[0];
            int y = current[1];
            int distance = current[2];
            
            if (x == targetX && y == targetY) {
                return distance / 2;
            }
            
            for (int[] direction: directions) {
                int nx = x + direction[0];
                int ny = y + direction[1];
                
                if (nx >= 0 && nx < SIZE * 2 && ny >= 0 && ny < SIZE * 2 && map[nx][ny] && !visited[nx][ny]) {
                    q.add(new int[]{nx, ny, distance + 1});
                    visited[nx][ny] = true;
                }
            }
        }
        return 0;
    }
}