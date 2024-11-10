import java.util.*;
import java.lang.*;
import java.io.*;

public class Main {

    private static int[][] adj;
    private static long result = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        adj = new int[n + 1][n + 1];

        StringTokenizer st;
        for (int i = 0; i < n - 1; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            adj[a][b] = c;
            adj[b][a] = c;
        }

        bfs(1, n);

        System.out.println(result);
    }

    private static void bfs(int start, int end) {
        Deque<long[]> q = new ArrayDeque<>();
        boolean[] visited = new boolean[end + 1];
        q.add(new long[]{start, 0});

        while(!q.isEmpty()) {
            long[] current = q.pollFirst();
            int vertex = (int) current[0];
            long cost = current[1];

            if (visited[vertex]) continue;
            visited[vertex] = true;
            
            result = Math.max(result, cost);

            for (int i = 1; i <= end; i++) {
                if (!visited[i] && adj[vertex][i] != 0) {
                    q.add(new long[]{i, cost + adj[vertex][i]});
                }
            }
        }
    }
}
