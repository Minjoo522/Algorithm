class Solution {
    public int solution(int a, int b) {
        int ab = Integer.parseInt(a + "" + b);
        int c = 2 * a * b;
        return ab > c ? ab : c;
    }
}