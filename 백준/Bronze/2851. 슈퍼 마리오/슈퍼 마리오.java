import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int score = 0;

        for (int i = 0; i < 10; i++) {
            int current = sc.nextInt();

            if (score + current >= 100) {
                if ((100 - score) >= ((score + current) - 100)) {
                    score += current;
                }
                break;
            }

            score += current;
        }

        System.out.println(score);
    }
}
