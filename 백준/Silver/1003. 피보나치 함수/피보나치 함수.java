import java.io.*;

public class Main {
    private static int[][] memo = new int[41][2];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());
        memo[0] = new int[]{1, 0};
        memo[1] = new int[]{0, 1};

        for (int i = 0; i < t; i++) {
            int n = Integer.parseInt(br.readLine());
            int[] result = dfs(n);
            System.out.println(result[0] + " " + result[1]);
        }
    }

    private static int[] dfs(int n) {
        if (memo[n][0] != 0 || memo[n][1] != 0) {
            return memo[n];
        }

        int[] left = dfs(n - 1);
        int[] right = dfs(n - 2);

        memo[n][0] = left[0] + right[0];
        memo[n][1] = left[1] + right[1];

        return memo[n];
    }
}