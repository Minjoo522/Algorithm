class Solution {
    public int solution(int[] num_list) {
        int result = num_list.length >= 11 ? 0 : 1;
        
        for (int i = 0; i < num_list.length; i++) {
            if (num_list.length >= 11) {
                result += num_list[i];
            } else {
                result *= num_list[i];
            }
        }
        return result;
    }
}