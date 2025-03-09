class Solution {
    public int solution(int n) {
        String s = String.valueOf(n);
        int result = 0;
        
        for (int i = 0; i < s.length(); i++) {
            result += Character.getNumericValue(s.charAt(i));
        }
        
        return result;
    }
}