import java.util.*;
import java.lang.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        int prev = 0;
        int[] holes = new int[n + 1];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= n; i++) {
            int current = Integer.parseInt(st.nextToken())+ i - 1; // 도토리 크기 하나씩 키우기(구멍 크기를 키운다)
            if (current > prev) {
                prev = current;
            }
            holes[i] = prev;
        }

        int q = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < q; i++) {
            int current = Integer.parseInt(st.nextToken());
            int left = 1;
            int right = n + 1;

            while (left < right) {
                int mid = (left + right) / 2;
                if (holes[mid] >= current) {
                    right = mid;
                } else {
                    left = mid + 1;
                }
            }
            sb.append(right).append(" ");
        }

        System.out.println(sb);
    }
}