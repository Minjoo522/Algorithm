import java.util.stream.IntStream;

class Solution {
    public int solution(int n) {
        if (n % 2 == 0) {
            return IntStream.rangeClosed(0, n)
                .filter(num -> num % 2 == 0)
                .map(num -> num * num)
                .sum();
        }
        return IntStream.rangeClosed(0, n)
            .filter(num -> num % 2 != 0)
            .sum();
    }
}