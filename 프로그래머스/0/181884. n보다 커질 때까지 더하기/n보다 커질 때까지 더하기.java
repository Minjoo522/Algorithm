class Solution {
    public int solution(int[] numbers, int n) {
        int result = 0;
        
        for (int num: numbers) {
            result += num;
            if (result > n) {
                break;
            }
        }
        return result;
    }
}