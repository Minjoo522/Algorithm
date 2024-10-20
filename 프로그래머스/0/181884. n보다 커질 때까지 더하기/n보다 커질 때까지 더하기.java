class Solution {
    public int solution(int[] numbers, int n) {
        int result = 0;
        
        for (int i = 0; result <= n; i++) {
            result += numbers[i];
        }
        return result;
    }
}