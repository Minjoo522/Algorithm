import java.util.*;
import java.lang.*;
import java.io.*;

public class Main {
    private static final int[][] directions = {{-1, 0}, {1, 0}, {0 , -1}, {0, 1}};
    private static int n;
    private static int[][] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        int[][] board = new int[n][n];
        dp = new int[n][n];

        StringTokenizer st;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
                dp[i][j] = -1;
            }
        }

        int result = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                result = Math.max(result, dfs(board, i, j));
            }
        }

        System.out.println(result);
    }

    private static int dfs(int[][] board, int i, int j) {
        if (dp[i][j] != -1) {
            return dp[i][j];
        }

        dp[i][j] = 1; // 셀 방문

        for (int[] direction : directions) {
            int ni = i + direction[0];
            int nj = j + direction[1];

            if (ni >= 0 && ni < n && nj >= 0 && nj < n && board[ni][nj] > board[i][j]) {
                dp[i][j] = Math.max(dp[i][j], 1 + dfs(board, ni, nj));
            }
        }
        return dp[i][j];
    }
}
