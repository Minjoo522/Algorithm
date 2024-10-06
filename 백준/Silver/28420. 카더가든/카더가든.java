import java.io.*;
import java.util.*;
import java.lang.*;

public class Main {

  public static void main(String[] args) throws IOException {
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      int result = Integer.MAX_VALUE;

      StringTokenizer st = new StringTokenizer(br.readLine());
      int N = Integer.parseInt(st.nextToken());
      int M = Integer.parseInt(st.nextToken());

      st = new StringTokenizer(br.readLine());
      int a = Integer.parseInt(st.nextToken());
      int b = Integer.parseInt(st.nextToken());
      int c = Integer.parseInt(st.nextToken());

      int[][] garden = new int[N + 1][M + 1];
      for (int i = 1; i <= N; i++) {
          st = new StringTokenizer(br.readLine());
          for (int j = 1; j <= M; j++) {
              garden[i][j] = Integer.parseInt(st.nextToken());
          }
      }

      int[][] prefix = new int[N + 1][M + 1];
      for (int i = 1; i <= N; i++) {
          for (int j = 1; j <= M; j++) {
              prefix[i][j] = garden[i][j] + prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1];
          }
      }

      for (int i = 1; i <= N - a + 1; i++) {
          for (int j = 1; j <= M - b - c + 1; j++) {
              result = Math.min(result, prefix_sum(prefix, i, j, i + a - 1, j + b + c - 1));
          }
      }

      for (int i = 1; i <= N - a - b + 1; i++) {
          for (int j = 1; j <= M - c - a + 1; j++) {
              result = Math.min(result, prefix_sum(prefix, i, j, i + a - 1, j + c - 1)
              + prefix_sum(prefix, i + a, j + c, i + a + b - 1, j + c + a - 1));
          }
      }

      for (int i = 1; i <= N - a - c + 1; i++) {
          for (int j = 1; j <= M - b - a + 1; j++) {
              result = Math.min(result, prefix_sum(prefix, i, j, i + a - 1, j + b - 1)
              + prefix_sum(prefix, i + a, j + b, i + a + c - 1, j + b + a - 1));
          }
      }

      System.out.println(result);
  }

    private static int prefix_sum(int[][] prefix, int x1, int y1, int x2, int y2) {
      return prefix[x2][y2] - prefix[x1 - 1][y2] - prefix[x2][y1 - 1] + prefix[x1 - 1][y1 - 1];
  }
}
