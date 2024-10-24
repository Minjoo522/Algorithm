import java.util.*;
import java.lang.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        List<Integer> cows = new ArrayList<>();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());

        for (int i = 0; i < n; i++) {
            cows.add(Integer.parseInt(br.readLine()) - 1);
        }

        // comulative sum, two-dimensional array
        int[][] counts = new int[n + 1][3];

        for (int i = 1; i < n + 1; i++) {
            counts[i][0] = counts[i - 1][0];
            counts[i][1] = counts[i - 1][1];
            counts[i][2] = counts[i - 1][2];

            counts[i][cows.get(i - 1)] += 1;
        }

        int[] result = new int[q];
        for (int i = 0; i < q; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());

            int holsteins = counts[end][0] - counts[start - 1][0];
            int huernseys = counts[end][1] - counts[start - 1][1];
            int jerseys = counts[end][2] - counts[start - 1][2];
            System.out.printf("%d %d %d\n", holsteins, huernseys, jerseys);
        }
    }
}