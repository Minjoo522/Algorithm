class Solution {
    public int solution(int m, int n, int[][] puddles) {
        int MOD = 1000000007;
        
        int[][] dp = new int[n + 1][m + 1];
        
        for (int[] puddle: puddles) {
            dp[puddle[1]][puddle[0]] = -1;
        }
        
        dp[1][1] = 1; // 시작점 설정!
        
        for (int i = 1; i < n + 1; i++) {
            for (int j = 1; j < m + 1; j++) {
                if (dp[i][j] == -1) {
                    dp[i][j] = 0;
                    continue;
                }
                if (i > 1) { // 위쪽에서 옴
                    dp[i][j] += dp[i - 1][j];
                }
                if (j > 1) { // 왼쪽에서 옴
                    dp[i][j] += dp[i][j - 1];
                }
                dp[i][j] %= MOD;
            }
        }
        return dp[n][m];
    }
}