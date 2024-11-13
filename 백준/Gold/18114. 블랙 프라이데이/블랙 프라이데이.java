import java.util.*;
import java.lang.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        n += 2;
        int c = Integer.parseInt(st.nextToken());

        int[] weights = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 2; i < n; i++) {
            weights[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(weights);

        boolean found = false;
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n - 1 && !found; j++) {
                int sum = weights[i] + weights[j];
                int rest = c - sum;
                found |= findRest(j + 1, n - 1, weights, rest);
            }
        }

        System.out.println(found ? 1 : 0);
    }

    private static boolean findRest(int left, int right, int[] weights, int rest) {
        while (left <= right) {
            int mid = (left + right) / 2;
            if (weights[mid] == rest) {
                return true;
            } else if (weights[mid] > rest) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return false;
    }
}