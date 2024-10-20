class Solution {
    public int solution(int[] num_list) {
        if (num_list.length >= 11) {
            return sum(num_list);
        }
        return prod(num_list);
    }
    
    private static int sum(int[] arr) {
        int result = 0;
        for (int num: arr) {
            result += num;
        }
        return result;
    }
    
    private static int prod(int[] arr) {
        int result = 1;
        for (int num: arr) {
            result *= num;
        }
        return result;
    }
}