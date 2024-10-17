import java.util.*;
import java.lang.*;
import java.io.*;

public class Main {

    static final int[] dx = {-1, -1, -1, 0, 0, 1, 1};
    static final int[] dy = {-1, 0, 1, -1, 1, -1, 1};
    static int result = 0;
    static int n;
    static int[][] visited;
    static int[][] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        visited = new int[n][n];
        arr = new int[n][n];
        int startX = 0, startY = 0;

        for (int i = 0; i < n; i++) {
            String[] line = br.readLine().split("");
            for (int j = 0; j < line.length; j++) {
                if (line[j].equals("#")) {
                    arr[i][j] = 1;
                } else if (line[j].equals(".")) {
                    arr[i][j] = 0;
                } else {
                    startX = i;
                    startY = j;
                    arr[i][j] = 1;
                }
            }
        }
        BFS(startX, startY);
        System.out.println(result);
    }

    static void BFS(int startX, int startY) {
        Deque<int[]> queue = new ArrayDeque<>();
        queue.add(new int[]{startX, startY});
        visited[startX][startY] = 1;

        while (!queue.isEmpty()) {
            int[] current = queue.removeFirst();
            int cx = current[0];
            int cy = current[1];

            for (int i = 0; i < 7; i++) {
                int nx = cx + dx[i];
                int ny = cy + dy[i];
                if (nx < 0 || ny < 0 || nx >= n || ny >= n) continue;
                if (visited[nx][ny] == 1 || arr[nx][ny] == 1) continue;
                visited[nx][ny] = 1;
                result++;
                queue.add(new int[]{nx, ny});
            }
        }
    }
}