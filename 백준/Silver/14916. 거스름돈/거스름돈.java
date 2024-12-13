import java.util.Arrays;
import java.util.Scanner;

public class Main {

    static int n;
    static int[] dp;
    static int maxValue = 100001;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();

        dp = new int[n + 1];
        Arrays.fill(dp, maxValue);

        int result = DP(n);

        System.out.println(result == maxValue ? -1 : result);
    }

    static int DP(int node) {
        if (node == 0) {
            return 0;
        }

        if (node < 0) {
            return maxValue;
        }

        if (dp[node] != maxValue) {
            return dp[node];
        }

        dp[node] = Math.min(dp[node], DP(node - 2) + 1);
        dp[node] = Math.min(dp[node], DP(node - 5) + 1);

        return dp[node];
    }
}
