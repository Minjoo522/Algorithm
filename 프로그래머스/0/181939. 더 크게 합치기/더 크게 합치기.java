class Solution {
    public int solution(int a, int b) {
        String a_str = String.valueOf(a);
        String b_str = String.valueOf(b);
        int ab = Integer.parseInt(a_str + b_str);
        int ba = Integer.parseInt(b_str + a_str);
        return ab > ba ? ab : ba;
    }
}