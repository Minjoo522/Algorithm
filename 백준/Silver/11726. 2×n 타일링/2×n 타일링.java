import java.util.*;

public class Main {
    static int[] memo = new int[1111];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.println(makeTile(n));
    }

    private static int makeTile(int n) {
        if (n == 1) return 1;
        if (n == 2) return 2;
        if (memo[n] != 0) return memo[n];
        memo[n] = (makeTile(n - 1) + makeTile(n - 2)) % 10007;
        return memo[n];
    }
}
