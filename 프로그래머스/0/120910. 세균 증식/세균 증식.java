class Solution {
    public int solution(int n, int t) {
        int result = n;
        
        while (t != 0) {
            result *= 2;
            t--;
        }
        
        return result;
    }
}