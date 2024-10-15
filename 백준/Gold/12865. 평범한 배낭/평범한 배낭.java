import java.util.*;
import java.lang.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int[][] stuffs = new int[N + 1][2];
        for (int i = 1; i < N + 1; i++) {
            st = new StringTokenizer(br.readLine());
            stuffs[i][0] = Integer.parseInt(st.nextToken());
            stuffs[i][1] = Integer.parseInt(st.nextToken());
        }

        int[][] dp = new int[N + 1][K + 1]; // 자동으로 0으로 초기화됨
        for (int i = 1; i < N + 1; i++) { // i = 물건 개수
            for (int j = 1; j < K + 1; j++) { // j = 배낭 무게
                if (j < stuffs[i][0]) {
                    dp[i][j] = dp[i -1][j];
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j], stuffs[i][1] + dp[i - 1][j - stuffs[i][0]]);
                }
            }
        }
        System.out.print(dp[N][K]);
    }
}