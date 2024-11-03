import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] times = new int[n];

        for (int i = 0; i < n; i++) {
            times[i] = sc.nextInt();
        }

        Arrays.sort(times);

        int[] prefixSum = new int[n];
        prefixSum[0] = times[0];
        for (int i = 1; i < n; i++) {
            prefixSum[i] = prefixSum[i - 1] + times[i];
        }

        int result = 0;
        for (int i = 0; i < n; i++) {
            result += prefixSum[i];
        }
        System.out.println(result);
    }
}